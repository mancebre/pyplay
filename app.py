#!/usr/bin/python

import jwt
from flask import Response
from libraries.authentication import Auth

from flask import Flask
from flask_restful import Api, Resource, reqparse, request
from routers.user import UserAPI

app = Flask(__name__)


# Here we can authenticate user
@app.before_request
def before_request():
    print(Auth.authenticate(Auth))
    return "NO ACCESS", 401


api = Api(app)

api.add_resource(UserAPI, "/user/<string:name>")

app.run(debug=True)
