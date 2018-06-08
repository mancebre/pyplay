
from database import MyDB

class User():

    def __init__(self):
        self.db = MyDB()

    def getActiveUserByName(self, name):
        sql = """SELECT * FROM users WHERE name = %s AND active = 1"""
        data = self.db.selectOne(sql, (name))
        
        if(data):
            return data
        else:
            return False

    def isUserExist(self, name):
        sql = """SELECT * FROM users WHERE name = %s"""
        data = self.db.selectOne(sql, (name))

        if(data):
            return True
        else:
            return False

    def createUser(self, name, age, occupation):
        sql = """INSERT INTO `users` (`id`, `name`, `age`, `occupation`, `active`) VALUES (NULL, %s, %s, %s, 1)"""
        self.db.query(sql, (name, age, occupation))
        user = {
            "name": name,
            "age": age,
            "occupation": occupation
        }
            
        return user

    def updateUser(self, name, age, occupation):
        user = {
            "name": name,
            "age": age,
            "occupation": occupation
        }

        sql = """UPDATE USERS SET name = %s, age = %s, occupation = %s WHERE name = %s"""
        self.db.query(sql, (name, age, occupation, name))
            
        return user

    def deactivateUser(self, name):
        sql = """UPDATE USERS SET active = 0 WHERE name = %s"""
        self.db.query(sql, (name))

        return True