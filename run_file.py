from db_connection_OOP import *
from db_products_OOP import DBProduct_table
from db_CRUDproducts_OOP import ProductTable
from db_customers import CustomerTable

customers = CustomerTable
product_table = DBProduct_table()
update_product = ProductTable()
#
print(CustomerTable.get_the_id(3))
#
#print(ProductTable.get_all())
#
# print(product_table.get_all('Chef'))
