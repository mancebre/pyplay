

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
        name = args["username"].encode('utf-8')
        is_username_taken = self.userModel.is_username_taken(self, name)
        if is_username_taken:
            return "User with username {} already exists".format(name), 400

        # Check is email taken
        email = args["email"]
        is_email_taken = self.userModel.is_email_taken(self, email)
        if is_email_taken:
            return "User with email address {} already exists".format(email), 400

        # Prepare data
        username = args["username"].encode('utf-8')
        password = args["password"].encode('utf-8')
        email = args["email"].encode('utf-8')
        firstname = args["firstname"].encode('utf-8')
        lastname = args["lastname"].encode('utf-8')
        newsletter = args["newsletter"].encode('utf-8')

        user_id = self.userModel.create_user(self, username, password, email, firstname, lastname, newsletter)
        role = User.assign_role(self, user_id, "User");
        return role, 201

    def assign_role(self, user_id, role):
        role_id = {
            'Admin': 2,
            'User': 3
        }.get(role, 9)

        return self.userModel.add_user_role(self, user_id, role_id)

    def update_user(self, user, data):
        user = self.userModel.update_user(self, user, data)
        return user, 200

    def deactivate_user(self, name):
        data = self.userModel.get_active_user(self, name)
        if data:
            self.userModel.deactivate_user(self, name)
            return "{} is deleted.".format(name), 200
        else:
            return "User not found", 404
