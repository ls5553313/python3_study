from pymysql import *

class Mysql_python:
    def __init__(self,database,
                 host="localhost",
                 user="root",
                 password="123456",
                 port=3306,
                 charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset=charset
        self.database=database

    def open(self):
        self.db = connect(host=self.host, 
                          user=self.user,
                          database =self.database,
                          password =self.password,
                          charset=self.charset)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def execute(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            self.db.commit()
            print("OK")
        except Exception as e:
            self.db.rollback();
            print("Failed",e)
        self.close()

    def select(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            result = self.cur.fetchall()
            self.db.commit()
            print("OK")
            return(result)
        except Exception as e:
            self.db.rollback();
            print("Failed",e)
        self.close()





