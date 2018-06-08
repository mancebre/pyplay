
from flask_restful import Api, Resource, reqparse
from controllers.user import User
from models.user import User as UserModel
from database import MyDB

class UserAPI(Resource):

    def __init__(self):
        self.db = MyDB()
        self.user = User
        self.userModel = UserModel

    def get(self, name):
        return self.user.return_user(self, name)

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        return self.user.add_user(self, name, args)

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        return self.user.update_user(self, name, args)

    def delete(self, name):
        return self.user.deactivate_user(self, name)