#!/usr/bin/python

import pymysql

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class MyDB(object):

    def __init__(self):
        self._db_connection = pymysql.connect("localhost","root","","testdb" )
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_connection.commit()

    def selectOne(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_cur.fetchone()

    def __del__(self):
        self._db_connection.close()


class User(Resource):

    def __init__(self):
        self.db = MyDB()

    def get(self, name):
        sql = """SELECT * FROM users WHERE name = %s AND active = 1"""
        data = self.db.selectOne(sql, (name))
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

        sql = """SELECT name FROM users WHERE name = %s"""
        data = self.db.selectOne(sql, (name))
        if(data):
            return "User with name {} already exists".format(name), 400

        sql = """INSERT INTO `users` (`id`, `name`, `age`, `occupation`, `active`) VALUES (NULL, %s, %s, %s, 1)"""
        self.db.query(sql, (name, args['age'], args['occupation']))
        user = {
            "name": name,
            "age": args['age'],
            "occupation": args['occupation']
        }

        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }

        sql = """UPDATE USERS SET name = %s, age = %s, occupation = %s WHERE name = %s"""
        self.db.query(sql, (name, args['age'], args['occupation'], name))
        return user, 200
        # TODO if user don't exists create it?
        # return user, 201

    def delete(self, name):

        sql = """SELECT * FROM users WHERE name = %s AND active = 1"""
        data = self.db.selectOne(sql, (name))
        if(data):
            sql = """UPDATE USERS SET active = 0 WHERE name = %s"""
            self.db.query(sql, (name))
            return "{} is deleted.".format(name), 200
        else:
            return "User not found", 404


api.add_resource(User, "/user/<string:name>")

app.run(debug=True)