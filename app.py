#!/usr/bin/python

from flask import Flask
from flask_restful import Api, Resource, reqparse
from routers.user import UserAPI

app = Flask(__name__)
api = Api(app)



api.add_resource(UserAPI, "/user/<string:name>")

app.run(debug=True)