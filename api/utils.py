import numpy as np
import os, json, random, math

#####################################################################
#######  The following are helper functions for computations  #######
#####################################################################

def get_euclidean_distance(coordinateA, coordinateB):
    differenceX = coordinateA[0] - coordinateB[0]
    differenceY = coordinateA[1] - coordinateB[1]
    return (differenceX * differenceX + differenceY * differenceY) ** 0.5

def state_count(state):
    count = -1
    while state:
        count += state%2
        state //= 2
    return count

#####################################################################
###########  The following are spots selection functions  ###########
#####################################################################

def get_typelist_by_compactness(compactness):
    type_list = []
    if compactness > 0.4: type_list.append('A')
    type_list.append('R')
    type_list = type_list + ['A'] * int(compactness*3 + 1)
    type_list.append('R')
    if compactness > 0.5: type_list.append('A')
    type_list.append('H')
    return type_list, len(type_list) - 3

def aggrgate_rating(spot):
    aggr_rating = math.exp(spot['rating']/2)
    return aggr_rating

def spot_selection(spots, num_items):
    # Randomized selection with high rating higher weighted
    randomized_spots = spots.copy()
    for spot_index in range(len(randomized_spots)):
        randomized_spots[spot_index]['customized_rating'] = aggrgate_rating(randomized_spots[spot_index]) + np.random.normal()
    randomized_spots = sorted(randomized_spots, key=lambda k: -k['customized_rating'])
    return randomized_spots[:num_items]

def get_restaurants_by_price_level(restaurants, price_level, num_items):
    if price_level == 0: price_level = None
    satisfied_restaurants = [r for r in restaurants if r['price_level'] == price_level]
    return spot_selection(satisfied_restaurants, num_items)

def get_attractions_by_outdoor(attractions, outdoor, num_items):
    indoor_attractions_types = ['place_of_worship', 'museum', 'premise', 'zoo', 'movie_theater', 'bakery']
    indoor_attractions, outdoor_attractions = [], []
    num_outdoor = int(outdoor * num_items)
    num_indoor = num_items - num_outdoor
    for attraction in attractions:
        is_indoor = False
        for indoor_type in indoor_attractions_types:
            if indoor_type in attraction['types']: is_indoor = True
        if is_indoor: indoor_attractions.append(attraction)
        else: outdoor_attractions.append(attraction)
    indoor_selection = spot_selection(indoor_attractions, num_indoor)
    outdoor_selection = spot_selection(outdoor_attractions, num_outdoor)
    total_selection = indoor_selection + outdoor_selection
    random.shuffle(total_selection)
    return total_selection

#####################################################################
########  The following minimal cost arrangement funcitons   ########
#####################################################################

def cost_criteria(spotA, spotB):
    Ax, Ay = spotA['geometry']['location']['lat'], spotA['geometry']['location']['lng']
    Bx, By = spotA['geometry']['location']['lat'], spotA['geometry']['location']['lng']
    geographical_distance = get_euclidean_distance((Ax, Ay), (Bx, By))
    return geographical_distance

def shortest_paths_recommandation(spots, type_requirement):
    num_spots = len(spots)
    num_visiting = len(type_requirement)
    num_states = (2 ** num_spots)
    dp_state_single = [(1e18, -1)] * num_spots
    dp_states = []
    for _ in range(num_states):
        dp_states.append(dp_state_single.copy())
    # Enumerate all possibilities via State Compression Dynamic Programming
    for spot_id in range(num_spots):
        if spots[spot_id]['id'][0] == type_requirement[0]:
            dp_states[int(2 ** spot_id)][spot_id] = (0, 0)
    best_final_state = (1e18, 0, 0)
    for visit_order in range(1, num_visiting):
        for state in range(num_states):
            if state_count(state) != visit_order: continue
            for spot_id in range(num_spots):
                # disregard impossible state
                spot = spots[spot_id]
                if spot['id'][0] != type_requirement[visit_order] or int((2 ** spot_id) & state) == 0: continue
                past_state = state - int(2 ** spot_id)
                best_plan = (1e18, -1)
                for source_id in range(num_spots):
                    if (int(2 ** source_id) & past_state) == 0: continue
                    past_cost, past_endpoint = dp_states[past_state][source_id]
                    cur_cost = cost_criteria(spots[source_id], spots[spot_id])
                    if past_cost + cur_cost < best_plan[0]:
                        best_plan = (past_cost + cur_cost, source_id)
                dp_states[state][spot_id] = best_plan
                if visit_order == num_visiting - 1 and best_plan[0] < best_final_state[0]:
                    best_final_state = (best_plan[0], state, spot_id)

    # Retrieve optimal plan under criteria
    routes = []
    final_state = (best_final_state[1], best_final_state[2])
    while final_state[0]:
        spot_id = spots[final_state[1]]['id']
        routes = [spot_id] + routes
        next_state = [int(final_state[0] - (2 ** final_state[1])), dp_states[final_state[0]][final_state[1]][1]]
        final_state = next_state
    return routes

#####################################################################
#######  The following is the main travel planning function   #######
#####################################################################

def travel_planner(num_days, price_level, outdoor, compactness, car, scooter, bike, place_ids = None, schedule = None):
    # Change directory later
    # Read parsed data from file
    data_path = os.path.join(os.getcwd(), '../data')
    objects = {
        'A' : json.load(open(os.path.join(data_path, 'Attraction.json'), 'r')),
        'H' : json.load(open(os.path.join(data_path, 'Homestay.json'), 'r')),
        'R' : json.load(open(os.path.join(data_path, 'Restaurant.json'), 'r')),
    }

    if place_ids == None:
        assert schedule == None
        candrate = 2
        type_list, num_attractions = get_typelist_by_compactness(compactness)
        attractions = get_attractions_by_outdoor(objects['A'], outdoor, num_days * num_attractions * candrate)
        restaurants = get_restaurants_by_price_level(objects['R'], price_level, num_days * candrate * 2)
        hotels = spot_selection(objects['H'], candrate)
        schedule = []
        for day in range(num_days):
            if day == num_days-1:
                type_list = type_list[:len(type_list)-3]
            spots = attractions[day*num_attractions: (day+1)*num_attractions] + restaurants[day*candrate: (day+1)*candrate] + [hotels[0]]
            schedule = schedule + shortest_paths_recommandation(spots, type_list)
        places = attractions + restaurants + hotels
        return {
            "status": "Success",
            "message": "Make a new {:d} day(s) plan in Taipei".format(num_days),
            "places": places,
            "schedule": schedule
        }
    else:
        places = [objects[place_id[0]][int(place_id[1:])] for place_id in place_ids]
        for place in places:
            if place['id'] not in schedule:
                schedule.insert(random.randrange(len(schedule)+1), place['id'])
