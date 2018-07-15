
from flask_restful import Resource, reqparse
from flask import request
from controllers.user import User
from controllers.recipe import Recipe
from models.user import User as UserModel
from models.recipe import Recipe as RecipeModel
from libraries.database import MyDB


# TODO Add recipe controller and model
# TODO recipe should have all (get, post, put, delete)


class RecipeAPI(Resource):

    def __init__(self):
        self.db = MyDB()
        self.user = User
        self.userModel = UserModel

    def get(self):
        email = request.args.get('email')
        password = request.args.get('password')
        args = {
            'email': email,
            'password': password
        }
        return args

    def post(self):
        # amount: recipeData.amount,
        # base: recipeData.base,
        # comment: recipeData.comment,
        # desired_strength: recipeData.desired_strength,
        # flavor: recipeData.flavor,
        # nicotine: {
        #     strength: recipeData.strength,
        #     pg: recipeData.pg,
        #     vg: recipeData.vg
        # },
        # pg: recipeData.pg,
        # sleep_time: recipeData.sleep_time,
        # vapeReady: recipeData.vapeReady,
        # vg: recipeData.vg,
        # wvpga: recipeData.wvpga

        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("amount")
        parser.add_argument("base")
        parser.add_argument("comment")
        parser.add_argument("desired_strength")
        parser.add_argument("flavor")
        parser.add_argument("nicotine")
        parser.add_argument("pg")
        parser.add_argument("sleep_time")
        parser.add_argument("vapeReady")
        parser.add_argument("vg")
        parser.add_argument("wvpga")
        args = parser.parse_args()

        return Recipe.save(self, args)

    # def put(self, name):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("age")
    #     parser.add_argument("occupation")
    #     args = parser.parse_args()
    #
    #     return self.user.update_user(self, name, args)
    #
    # def delete(self, name):
    #     return self.user.deactivate_user(self, name)
