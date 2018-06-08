
from database import MyDB
from models.user import User as UserModel

class User():

    def __init__(self):
        self.db = MyDB()
        self.userModel = UserModel

    def returnUser(self, name):
        data = self.userModel.getActiveUserByName(self, name)
        if(data):
            user = {
                "name": data[1],
                "age": data[2],
                "occupation": data[3]
            }
            return user, 200
        else:
            return "User not found", 404

    def addUser(self, name, args):
        isUserExist = self.userModel.isUserExist(self, name)
        if(isUserExist):
            return "User with name {} already exists".format(name), 400

        user = self.userModel.createUser(self, name, args['age'], args['occupation'])
        return user, 201

    def updateUser(self, name, args):
        user = self.userModel.updateUser(self, name, args['age'], args['occupation'])
        return user, 200

    def deactivateUser(self, name):
        data = self.userModel.getActiveUserByName(self, name)
        if(data):
            self.userModel.deactivateUser(self, name)
            return "{} is deleted.".format(name), 200
        else:
            return "User not found", 404