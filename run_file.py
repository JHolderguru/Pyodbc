from db_connection_OOP import *
from db_products_OOP import DBProduct_table
from db_CRUDproducts_OOP import ProductTable
from db_customers import CustomerTable
from flask_sqlalchemy import SQLAlchemy


# #1) Fetching Data from Customer Table
#
# Customer = CustomerTable()
# for data in Customer.get_the_id('ANTON'):
#     print(data)
#
# #1a) Fetching all the data from the customer
# # for data in Customer.get_all():
# #     print(data)
#
# #1b) Fetching Particular data from the customer(purse in the name)
# for data in Customer.get_all('Elizabeth'):
#     print(data)
#
#
# #2) Fetching Data from Products Table
#
# products = ProductTable()
# for data in products.get_by_id(3):
#     print(data)
#
# #or  and pass the id
#
# print(products.get_by_id(2))
#
# #2a)Fetching all the Data from the ProductTable()
# # for data in (products.get_all()):
# #     print(data)
#



#3) Now we want to input data into the table
new_entry = ProductTable()
# cus_entry = CustomerTable()

while True:
    user_input = input("Press any key to continue or press 'x' to exit: ")
    while user_input != 'x':
        ProductID = int(input("Enter product ID number or press 'x' to abort"))
        ProductName = (input('insert the name please'))
        SupplierID = int(input())
        CategoryID = int(input())
        QuantityPerUnit = int(input())
        UnitPrice = float(input())
        UnitsInStock = int(input())
        UnitsOnOrder = int(input())
        ReOrderLevel = int(input())
        Discontinued = int(input())
        print(new_entry.create_entry(ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice,
                                     UnitsInStock, UnitsOnOrder, ReOrderLevel,Discontinued))
        while user_input == 'x':
            break
    if user_input == 'x':
        break


















# customers = CustomerTable
# product_table = DBProduct_table()
# update_product = ProductTable()
# #
# print(CustomerTable.get_the_id(3))
# #
# #print(ProductTable.get_all())
# #
# # print(product_table.get_all('Chef'))


#ALchemy tests
# app = Flask(__name__)
#
# app.config['Northwind'] = sqlite:////absolute/path/to/foo.db
# app.config['Northwind'] =  sql:////databases2.spartaglobal.academy.db
# db = SQLAlchemy(app)


