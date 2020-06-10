import pyodbc

#1) DB server connection variables
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_string ='DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
# print(db_string)

#2Est a connect
py_connect2 = pyodbc.connect(db_string)
#3)makescursor(this keeps state)
#making a cursor

cursor = py_connect2.cursor()
print(cursor)


# 4)Fetchone() ---remember cursor maintains state
# query_result = cursor.execute('SELECT * FROM Products')
#
# print(query_result)
#
#
# # .fetchone() --> output next 1 pyodbc.Row -- remember cursor maintains state
# # if you want to get back to the start, you need a new cursor or to run the execute command again.
# print(query_result.fetchone()) # less one entry in the cursor
# print(query_result.fetchone()) # less one entry in the cursor \\\\\\\\\
# data_point_card = query_result.fetchone()
#
# # this one entry of data is a 'pyodbc.Row' object
# print(type(data_point_card))
# # behaves like an iterable list - organised with index
# print(data_point_card[1])
# # also behave like a oop object, where the initialized parameters/attribute are the column names
#print(data_point_card.ProductName)

# Search documentation/or internet to use a for loop to get our all of the data using the .fetchone() method


# .fetchall --> output all the pyodbc.Row (s) into list -- remember cursor maintains state
# DANGEROUS -- Do not use in real life. So also not here :)
# list_of_all_rows = query_result.fetchall()
#print(len(list_of_all_rows))
# if you have a million entries this will cause your server to run out of intantanous memory and wil crash.

# # print(query_result.fetchall())
# # print(query_result.fetchall())
# all_results_list = query_result.fetchall()
#
# for data in all_results_list:
#     print(data.ProductName, 'costs: ', data.UnitPrice)



# The Better way of getting out all your data
# query_result = [10, 10, 100, 30, 50, None]

# query_result = cursor.execute('SELECT UnitPrice FROM Products')

# query_result = cursor.execute('SELECT * FROM Products')
#
# while True:
# #         use our uery results or cursoe with query reulst and
# fetch one at a time and
#   do whatever we want/need with that data point - print it ? get out the price? add a discount?
#   Stop the iteration when there is no more data
#           ----> or when the data point is None (python) ( null is in SQL)
#     row = query_result.fetchone()
#     if row == None:
#         break
#     print(row.ProductName, 'NOW ONLY', float(row.UnitPrice) * 0.50)

#The way you design or the way yo fetch data will have an impact performance and price at the end of the month