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

query_result = cursor.execute('SELECT * FROM Products')

while True:
#         use our uery results or cursoe with query reulst and
# fetch one at a time and
#   do whatever we want/need with that data point - print it ? get out the price? add a discount?
#   Stop the iteration when there is no more data
#           ----> or when the data point is None (python) ( null is in SQL)
    row = query_result.fetchone()
    if row == None:
        break
    print(row.ProductName, 'NOW ONLY', float(row.UnitPrice) * 0.50)

#The way you design or the way yo fetch data will have an impact performance and price at the end of the month