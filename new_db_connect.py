import pyodbc

# Make a new connection
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_string = 'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

# making a new cursor
py_connect2 = pyodbc.connect(db_string)
cursor = py_connect2.cursor()
print(cursor)

# Q1 - How many orders in NWDB?
# Query:
query_result = cursor.execute('SELECT * FROM Orders ')

# Response: 830
# print(len(query_result.fetchall()))


# Q2 - How many orders that the Ship City is Rio de Janeiro?
# Query:
query_result2 = cursor.execute("SELECT * FROM Orders"
                               " WHERE ShipCity= 'Rio de Janeiro'")
# Response: 34
# print(len(query_result2.fetchall()))

# Q3 - Select all orders that the Ship City is Rio de Janeiro or Reims?
# Query:
query_result3 = cursor.execute("SELECT * FROM Orders "
                               "WHERE ShipCity = 'Rio de Janeiro' OR ShipCity= 'Reims' ")
# Response:
print(query_result3.fetchall())

# Q4 - Select all of the entries where the Company name has a z or a Z in the table of Customers
# Query:
# query_result4 = cursor.execute("SELECT * Customers WHERE CompanyName LIKE '%z%' OR CompanyName LIKE '%Z%' ")

# Response:
# print(query_result4.fetchall())
