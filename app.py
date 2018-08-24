#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jwt
from flask import Response, jsonify
from libraries.authentication import Auth
from flask_cors import CORS, cross_origin

from flask import Flask
from flask_restful import Api, Resource, reqparse, request
from routers.user import UserAPI
from routers.recipe import RecipeAPI
from routers.recipes import RecipesAPI

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})


# Here we can authenticate user
# @app.before_request
# def before_request():
#     print(Auth.authenticate(Auth))
#     return "NO ACCESS", 401


api = Api(app)

api.add_resource(UserAPI, "/user/")
api.add_resource(RecipeAPI, "/recipe/")
api.add_resource(RecipesAPI, "/recipes/")

app.run(debug=True)
