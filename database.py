

import pymysql


class MyDB(object):

    def __init__(self):
        self._db_connection = pymysql.connect("localhost","root","","testdb" )
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_connection.commit()

    def select_one(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_cur.fetchone()

    def __del__(self):
        self._db_connection.close()