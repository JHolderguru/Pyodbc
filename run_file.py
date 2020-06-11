from db_connection_OOP import *
from db_products_OOP import DBProduct_table
from db_CRUDproducts_OOP import ProductTable
from db_customers import CustomerTable
from flask_sqlalchemy import SQLAlchemy


#1) Fetching Data from Customer Table

Customer = CustomerTable()
for data in Customer.get_the_id('ANTON'):
    print(data)


#2) Fetching Data from Products Table

products = ProductTable()
for data in products.get_by_id(3):
    print(data)

#or  and pass the id

print(products.get_by_id(2))



#
# new_entry = ProductTable()
# cus_entry = CustomerTable()
#
# while True:
#     user_input = input("Press any key to continue or press 'x' to exit: ")
#     while user_input != 'x':
#         user_input_1 = input("Enter product name or press 'x' to abort")
#         user_input_2 = int(input())
#         user_input_3 = int(input())
#         user_input_4 = input()
#         user_input_5 = int(input())
#         user_input_6 = int(input())
#         user_input_7 = int(input())
#         user_input_8 = int(input())
#         print(new_entry.create_entry(user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6,
#                                      user_input_7, user_input_8))
#         while user_input_1 == 'x':
#             break
#     if user_input == 'x':
#         break
#

















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


