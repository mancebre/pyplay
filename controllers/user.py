

from models.user import User as UserModel
from libraries.token import Token


class User:

    def __init__(self):
        self.userModel = UserModel

    def return_user(self, args):
        user_data = self.userModel.get_active_user(self, args)
        if user_data:
            # Get user roles by user id
            user_roles = self.userModel.get_user_roles(self, user_data["user_id"])

            if user_roles:
                payload = {
                    "user_data": user_data,
                    "user_roles": user_roles
                }

                token = Token(payload)

                result = {
                    'token': token.token
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
        data = self.userModel.get_active_user(self, name)
        if data:
            self.userModel.deactivate_user(self, name)
            return "{} is deleted.".format(name), 200
        else:
            return "User not found", 404
