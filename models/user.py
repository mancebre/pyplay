
from libraries.database import MyDB


# TODO Make this like user object


class User:

    def __init__(self):
        self.db = MyDB()

    def get_user_roles(self, userId):
        sql = """SELECT * FROM roles r INNER JOIN user_roles ur ON ur.role_id = r.id WHERE user_id = %s"""
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
    def is_username_taken(self, name):
        sql = """SELECT * FROM users WHERE username = %s"""
        data = self.db.select_one(sql, name)

        if data:
            return True
        else:
            return False

    def is_email_taken(self, email):
        sql = """SELECT * FROM users WHERE email = %s"""
        data = self.db.select_one(sql, email)

        if data:
            return True
        else:
            return False

    def create_user(self, username, password, email, firstname, lastname, newsletter):
        sql = """INSERT INTO `users` (`username`, `password`, `email`, `firstname`, `lastname`, `active`, `newsletter`) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        result = self.db.insert(sql, (username, password, email, firstname, lastname, 1, newsletter))
            
        return result

    def add_user_role(self, user_id, role_id):
        sql = """INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s);"""
        result = self.db.insert(sql, (user_id, role_id))

        return result

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
