import pyodbc

class MSDBconnection():

    def __init__(self, database ='Northwind', server='databases2.spartaglobal.academy', password='Passw0rd2018'):
        # 1) DB server connection variables
        self.server = server
        self.database = database
        self.username = 'SA'
        self.password = password
        self.conn = self._establish_connection()

    #2) Establishing the connection
    def _establish_connection(self):
        connection = pyodbc.connect()
        'DRIVER={SQL Server};SERVER=' + self server + ';DATABASE=' + self database + ';UID=' + self username + ';PWD=' +self password
        # print(db_string)

    def sql_query(self, sql_string):
        #call method to filter out DROP table and DELETE * and only allow certain SQL queries
        return self.cursor.execute(sql_string)

# nwind = MSDBconnection()
# print(nwind.sql_query('SELF * FROM PRODUCTS'))
#
# results =nwind.sql_query('SELECT * FROM PRODUCTS')
#
# while True:
#    if row = None
