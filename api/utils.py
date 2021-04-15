import numpy as np
import os, json, random, math

###################################################
#######  Helper functions for computations  #######
###################################################

# Return the euclidean distance of two coordinates
def get_euclidean_distance(coordinateA, coordinateB):
    differenceX = coordinateA[0] - coordinateB[0]
    differenceY = coordinateA[1] - coordinateB[1]
    return (differenceX * differenceX + differenceY * differenceY) ** 0.5

# Helper function of shortest path scheduling
def state_count(state):
    count = -1
    while state:
        count += state%2
        state //= 2
    return count

###################################################
###########  Spots selection functions  ###########
###################################################

# Return attraction-restaurant-hotel type schedule by compactness
def get_typelist_by_compactness(compactness, start_time, back_time):
    type_list = []
    restaurant_and_hotel_cnt = 0
    if int(start_time[:2]) < 11:
        if compactness > 0.4: type_list.append('A')
    if int(start_time[:2]) < 13:
        type_list.append('R')
        type_list = type_list + ['A'] * int(compactness*3 + 1)
        restaurant_and_hotel_cnt += 1
    if int(back_time[:2]) > 18:
        type_list.append('R')
        if compactness > 0.5: type_list.append('A')
        restaurant_and_hotel_cnt += 1
    if int(back_time[:2]) > 23:
        type_list.append('H')
        restaurant_and_hotel_cnt += 1
    return type_list, len(type_list) - restaurant_and_hotel_cnt

# Return customized spot rating 
def aggrgate_rating(spot, places = None):
    # Reference google users rating
    aggr_rating = math.exp(spot['rating']/2)
    # Reference app user input 
    if places != None and spot in places:
        aggr_rating += 1000
    # May add other criteria by collecting past usage information 
    return aggr_rating

# Return candidate spots
def spot_selection(spots, num_items, places = None):
    # Randomized selection with sampling higher rating with higher chance
    randomized_spots = spots.copy()
    for spot_index in range(len(randomized_spots)):
        randomized_spots[spot_index]['customized_rating'] = aggrgate_rating(randomized_spots[spot_index], places = places) + np.random.normal()
    randomized_spots = sorted(randomized_spots, key=lambda k: -k['customized_rating'])
    selected_spots = randomized_spots[:num_items]
    return sorted(selected_spots, key=lambda k: k['geometry']['location']['lat'])

# Return selected restaurants
def get_restaurants_by_price_level(restaurants, price_level, num_items, places = None):
    # Filter by indicated price level
    if price_level == 0: price_level = None
    satisfied_restaurants = [r for r in restaurants if r['price_level'] == price_level]
    return spot_selection(satisfied_restaurants, num_items, places = places)

# Return selected attractions
def get_attractions_by_outdoor(attractions, outdoor, num_items, places = None):
    # Split into indoor and outdoor attractions by indicated ratio
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
    indoor_selection = spot_selection(indoor_attractions, num_indoor, places = places)
    outdoor_selection = spot_selection(outdoor_attractions, num_outdoor, places = places)
    total_selection = indoor_selection + outdoor_selection
    total_selection = sorted(total_selection, key=lambda k: k['geometry']['location']['lat'])
    return total_selection

#######################################################
########  Minimal cost arrangement funcitons   ########
#######################################################

# Return cost of travelling
def cost_criteria(spotA, spotB):
    # Consider geographical distance
    Ax, Ay = spotA['geometry']['location']['lat'], spotA['geometry']['location']['lng']
    Bx, By = spotB['geometry']['location']['lat'], spotB['geometry']['location']['lng']
    geographical_distance = get_euclidean_distance((Ax, Ay), (Bx, By))
    # May consider other criteria by collecting past usage information 
    return geographical_distance

# Efficient algorithm for finding optimal paths
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

################################################
#######  Main travel planning function   #######
################################################

# Return the scheduled tour
def travel_scheduler(num_days, start_time, back_time, compactness, candrate, type_list, num_attractions, attractions, restaurants, hotels):
    schedule = []
    for day in range(num_days):
        day_start, day_end = "0000", "2400"
        if day == 0: day_start = start_time
        if day == num_days-1: day_end = back_time
        day_type_list, types = get_typelist_by_compactness(compactness, day_start, day_end)
        spots = attractions[day*num_attractions: (day+1)*num_attractions] + restaurants[day*candrate*2: (day+1)*candrate*2] + [hotels[0]]
        schedule = schedule + shortest_paths_recommandation(spots, day_type_list)
    places = attractions + restaurants + hotels
    return places, schedule

# Main planner function
def travel_planner(num_days, price_level, outdoor, compactness, start_time, back_time, place_ids = None, schedule = None):
    # Read parsed data from file
    data_path = os.path.join(os.getcwd(), './data')
    objects = {
        'A' : json.load(open(os.path.join(data_path, 'Attraction.json'), 'r')),
        'H' : json.load(open(os.path.join(data_path, 'Homestay.json'), 'r')),
        'R' : json.load(open(os.path.join(data_path, 'Restaurant.json'), 'r')),
    }

    if place_ids == None:
        assert schedule == None
        candrate = 2
        type_list, num_attractions = get_typelist_by_compactness(compactness, "0000", "2400")
        attractions = get_attractions_by_outdoor(objects['A'], outdoor, num_days * num_attractions * candrate)
        restaurants = get_restaurants_by_price_level(objects['R'], price_level, num_days * candrate * 2)
        hotels = spot_selection(objects['H'], candrate)
        return travel_scheduler(num_days, start_time, back_time, compactness, candrate, type_list, num_attractions, attractions, restaurants, hotels)

    else:
        places = [objects[place_id[0]][int(place_id[1:])] for place_id in place_ids]
        candrate = 1
        type_list, num_attractions = get_typelist_by_compactness(compactness, "0000", "2400")
        attractions = get_attractions_by_outdoor(objects['A'], outdoor, num_days * num_attractions * candrate, places = places)
        restaurants = get_restaurants_by_price_level(objects['R'], price_level, num_days * candrate * 2, places = places)
        hotels = spot_selection(objects['H'], candrate, places = places)
        return travel_scheduler(num_days, start_time, back_time, compactness, candrate, type_list, num_attractions, attractions, restaurants, hotels)

