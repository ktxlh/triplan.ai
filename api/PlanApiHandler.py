from datetime import date

from flask_restful import Api, Resource, reqparse

from api.utils import dummy_planner


class PlanApiHandler(Resource):
  def post(self):
    print(self)
    parser = reqparse.RequestParser()

    parser.add_argument('departure_date', type=str, required=True)  # e.g. 2021-04-20
    parser.add_argument('return_date', type=str, required=True)     # e.g. 2021-04-23
    parser.add_argument('city', type=str, required=True)            # e.g. Taipei

    # preferences - general
    parser.add_argument('price_level', type=int, default=2)         # The price level of the place, on a scale of 0 to 4
    parser.add_argument('outdoor', type=float, default=0.5)         # 0.0 to 1.0
    parser.add_argument('compactness', type=float, default=0.5)     # 0.0 to 1.0
    # preferences - transportation  ## TODO: backend won't use these, right?
    parser.add_argument('car', type=bool, default=True)
    parser.add_argument('scooter', type=bool, default=True)
    parser.add_argument('bike', type=bool, default=True)

    # for update only
    parser.add_argument('place_ids', type=str, action='append')        # id of the seleceted places (multiple & ordered)
    parser.add_argument('schedule', type=str, action='append')      # id of the current schedule (multiple & ordered)

    args = parser.parse_args()

    print(args)

    update = args['place_ids'] and args['schedule']
    if update:
      message = "Update with place_ids: {} and schedule: {}".format(','.join(args['place_ids']), ','.join(args['schedule']))
    else:
      message = "Make a new plan from {} to {} in {}".format(args['departure_date'], args['return_date'], args['city'])

    dd = [int(e) for e in args['departure_date'].split('-')]
    rd = [int(e) for e in args['return_date'].split('-')]
    n_days = (date(*rd) - date(*dd)).days + 1

    places, schedule = dummy_planner(
        n_days, args['price_level'], args['outdoor'], args['compactness'], 
        args['car'], args['scooter'], args['bike'], 
        args['place_ids'], args['schedule']
    )
    final_ret = {
        "status": "Success", 
        "message": message,
        "places" : places,
        "schedule" : schedule,
    }

    return final_ret
