import os, json, random

def dummy_planner(n_days, price_level, outdoor, compactness, start_time, back_time, place_ids = None, schedule = None):

    data_path = os.path.join(os.getcwd(), 'data')
    objects = {
        'A' : json.load(open(os.path.join(data_path, 'Attraction.json'), 'r')),
        'H' : json.load(open(os.path.join(data_path, 'Homestay.json'), 'r')),
        'R' : json.load(open(os.path.join(data_path, 'Restaurant.json'), 'r')),
    }

    if place_ids == None:
        assert schedule == None
        random.seed(int(155 * (outdoor + 1) * (price_level + 1)))
        places = [pp
            for i in range(n_days)
            for p in [
                random.sample(objects['A'], k = 1) if compactness > 0.5 else [],
                random.sample(objects['R'], k = 1),
                random.sample(objects['A'], k = int(3 * compactness + 1)),
                random.sample(objects['R'], k = 1),
                random.sample(objects['A'], k = 1) if compactness > 0.5 else [],
                random.sample(objects['H'], k = 1) if i < n_days - 1 else [],
            ] 
            for pp in p
        ]
        schedule = [p['id'] for p in places]
        places.extend([p for t in ['A', 'H', 'R'] for p in random.sample(objects[t], k = 5)])
    else:
        places = [objects[place_id[0]][int(place_id[1:])] for place_id in place_ids]
        for place in places:
            if place['id'] not in schedule:
                schedule.insert(random.randrange(len(schedule)+1), place['id'])

    return places, schedule
