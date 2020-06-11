# import pyodbc

# As a user I can C R from the CRUD Products table
from db_connection_OOP import MSDBconnection


class ProductTable(MSDBconnection):

    def create_entry(self, ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit,UnitPrice,
                     UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued):
        return self.sql_query(f"""INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit,UnitPrice,
                               UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
                               VALUES (f{ProductName},'{ProductName}', {SupplierID}, {CategoryID}, '{QuantityPerUnit}',{UnitPrice}, 
                                {UnitsInStock}, {UnitsOnOrder}, {ReorderLevel}, {Discontinued})""").commit

    def get_by_id(self, id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(id)).fetchone()

    def get_all(self, product_name=None):
        result_list = []

        if product_name == None:
            q_result = self.sql_query('SELECT * FROM Products')
        else:
            q_result = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE %'{product_name}'%")

        while True:
            row = q_result.fetchone()
            if row == None:
                break
            result_list.append(row)
        return result_list

    def update_db(self, column_1, val_1, column_2, condition):
        return self.sql_query(f"UPDATE Products SET {column_1} = '{val_1}' WHERE {column_2} = '{condition}'").commit


# products = ProductTable()


# print(products.get_all())
#
# print(products.get_by_id(2))
# # #
# print(product_table.get_all())
# #
# print(product_table.get_all('Chef'))
