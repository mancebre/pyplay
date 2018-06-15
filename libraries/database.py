

import pymysql


class MyDB(object):

    def __init__(self):
        self._db_connection = pymysql.connect("localhost","root","","testdb", use_unicode=True, charset="utf8" )
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_connection.commit()

    def insert(self, query, params):
        self._db_cur.execute(query, params)
        self._db_connection.commit()
        return self._db_cur.lastrowid

    def select_one(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_cur.fetchone()

    def select(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_cur.fetchall()

    def last_id(self):
        return self._db_cur.lastrowid

    def __del__(self):
        self._db_connection.close()
