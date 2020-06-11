import pyodbc

from db_connect import *


class MSDBconnection():

    def __init__(self, database='Northwind', server='databases2.spartaglobal.academy', username='SA',
                 password='Passw0rd2018'):
        # 1) DB server connection variables
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        # making connection and cursors
        self.conn = self._establish_connection()
        self.cursor = self.conn.cursor()

        # 2) establishing the connection

    def _establish_connection(self):
        py_connect2 = 'DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password
        return pyodbc.connect(py_connect2)

    def sql_query(self, sql_string):
        # call method to filter out DROP table and DELETE * and only allow certain SQL queries
        return self.cursor.execute(sql_string)


nwind = MSDBconnection()
# print(nwind.sql_query('SELECT * FROM PRODUCTS'))
# #
# results = nwind.sql_query('SELECT * FROM PRODUCTS')
# print(results)
# # #
# while True:
#      row = results.fetchone()
# #
#      if row == None:
#          break
#      print(row.ProductName)
