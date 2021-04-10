from flask_restful import Api, Resource, reqparse

class DefaultApiHandler(Resource):
  def get(self):
    return {
        'resultStatus': 'SUCCESS',
        'message': "Default Api Handler"
    }
