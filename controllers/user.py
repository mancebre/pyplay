

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

    def add_user(self, args):
        # Check is username taken
        name = args["username"]
        is_username_taken = self.userModel.is_username_taken(self, name)
        if is_username_taken:
            return "User with username {} already exists".format(name), 400

        # Check is email taken
        email = args["email"]
        is_email_taken = self.userModel.is_email_taken(self, email)
        if is_email_taken:
            return "User with email address {} already exists".format(email), 400

        # Prepare data
        username = args["username"]
        password = args["password"]
        email = args["email"]
        firstname = args["firstname"]
        lastname = args["lastname"]
        newsletter = args["newsletter"]

        user = self.userModel.create_user(self, username, password, email, firstname, lastname, newsletter)
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
