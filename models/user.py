
from libraries.database import MyDB


# TODO Make this like user object


class User:

    def __init__(self):
        self.db = MyDB()

    def get_user_roles(self, userId):
        sql = """SELECT * FROM roles WHERE user_id = %s"""
        data = self.db.select(sql, (userId))

        if data:
            roles = list()
            for role in data:
                roles.append({
                    "role_id": role[0],
                    "role_name": role[1]
                })
            return roles
        else:
            return False

    def get_active_user(self, args):
        sql = """SELECT * FROM users WHERE email = %s AND password = %s AND active = 1"""
        data = self.db.select_one(sql, (args['email'], args["password"]))
        
        if data:
            userData = {
                "user_id": data[0],
                "username": data[1],
                "email": data[3],
                "firstname": data[4],
                "lastname": data[5]
            }
            return userData
        else:
            return False

    # Check by username
    def is_user_exist(self, name):
        sql = """SELECT * FROM users WHERE name = %s"""
        data = self.db.select_one(sql, name)

        if data:
            return True
        else:
            return False

    def create_user(self, name, age, occupation):
        sql = """INSERT INTO `users` (`id`, `name`, `age`, `occupation`, `active`) VALUES (NULL, %s, %s, %s, 1)"""
        self.db.query(sql, (name, age, occupation))
        user = {
            "name": name,
            "age": age,
            "occupation": occupation
        }
            
        return user

    def update_user(self, name, age, occupation):
        user = {
            "name": name,
            "age": age,
            "occupation": occupation
        }

        sql = """UPDATE USERS SET name = %s, age = %s, occupation = %s WHERE name = %s"""
        self.db.query(sql, (name, age, occupation, name))
            
        return user

    def deactivate_user(self, name):
        sql = """UPDATE USERS SET active = 0 WHERE name = %s"""
        self.db.query(sql, name)

        return True
