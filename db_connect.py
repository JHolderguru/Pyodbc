import pyodbc

#1) DB server connection variables
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_string ='DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
# print(db_string)


#3)makescursor(this keeps state)
#making a cursor
py_connect2 = pyodbc.connect(db_string)
cursor = py_connect2.cursor()
print(cursor)


# 4)Fetchone() ---remember cursor maintains state
query_result = cursor.execute('SELECT * FROM Products')
print(query_result.fetchone()) #less one entry in the cursor\\\\\\\
print(query_result.fetchone()) #less one entry in the cursor
#if you want to get back to the start, you need a new cursor or to run the execute commang again
data_point_card = query_result.fetchone()
#this one entry point of data

all_results_list = query_result.fetchall()

#this one entry of data is a pyodbc.Row object
print(type(data_point_card))
#
#behaves like a iterable list -organised with index
print(data_point_card[1])
#
#
for data_point_card in all_results_list:
    print(data_point_card.ProductName,'costs', data_point_card.UnitPrice)