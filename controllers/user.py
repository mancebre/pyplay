
from libraries.database import MyDB
from models.user import User as UserModel


class User:

    def __init__(self):
        self.db = MyDB()
        self.userModel = UserModel

    def return_user(self, args):
        data = self.userModel.get_active_user_by_name(self, args)
        if data:
            user = {
                "username": data[1],
                "email": data[3],
                "firstname": data[4],
                "lastname": data[5]
            }
            result = {
                'userData': user,
                'token': 123456
            }
            return result, 200
        else:
            return "User not found", 404

    def add_user(self, name, args):
        is_user_exist = self.userModel.is_user_exist(self, name)
        if is_user_exist:
            return "User with name {} already exists".format(name), 400

        user = self.userModel.create_user(self, name, args['age'], args['occupation'])
        return user, 201

    def update_user(self, name, args):
        user = self.userModel.update_user(self, name, args['age'], args['occupation'])
        return user, 200

    def deactivate_user(self, name):
        data = self.userModel.get_active_user_by_name(self, name)
        if data:
            self.userModel.deactivate_user(self, name)
            return "{} is deleted.".format(name), 200
        else:
            return "User not found", 404
