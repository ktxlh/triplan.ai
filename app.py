from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.DefaultApiHandler import DefaultApiHandler
from api.PlanApiHandler import PlanApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

api.add_resource(DefaultApiHandler, '/')
api.add_resource(PlanApiHandler, '/plan')