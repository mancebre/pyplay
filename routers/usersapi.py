
from flask_restful import Api, Resource, reqparse
from database import MyDB
from controllers.users import Users

class UserAPI(Resource):

    def __init__(self):
        self.db = MyDB()
        self.users = Users

    def get(self, name):
        data = self.users.getActiveUserByName(self, name)
        if(data):
            user = {
                "name": data[1],
                "age": data[2],
                "occupation": data[3]
            }
            return user, 200
        else:
            return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        isUserExist = self.users.isUserExist(self, name)
        if(isUserExist):
            return "User with name {} already exists".format(name), 400

        user = self.users.createUser(self, name, args['age'], args['occupation'])
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        
        user = self.users.updateUser(self, name, args['age'], args['occupation'])
        return user, 200

    def delete(self, name):
        data = self.users.getActiveUserByName(self, name)
        if(data):
            self.users.deactivateUser(self, name)
            return "{} is deleted.".format(name), 200
        else:
            return "User not found", 404