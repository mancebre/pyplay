
from libraries.database import MyDB


class User:

    def __init__(self):
        self.db = MyDB()

    def get_active_user_by_name(self, name):
        sql = """SELECT * FROM users WHERE name = %s AND active = 1"""
        data = self.db.select_one(sql, (name))
        
        if data:
            return data
        else:
            return False

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
