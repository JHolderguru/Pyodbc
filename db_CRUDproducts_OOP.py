# import pyodbc

# As a user I can C R from the CRUD Products table
from db_connection_OOP import MSDBconnection


class ProductTable(MSDBconnection):

    def create_entry(self, ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit,
                     UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued):
        return self.sql_query(f"""INSERT INTO Products (ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit,
                               UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
                               VALUES (f{ProductID}, '{ProductName}', {SupplierID}, {CategoryID}, '{QuantityPerUnit}', 
                                {UnitsInStock}, {UnitsOnOrder}, {ReorderLevel}, {Discontinued})""")

    def get_by_id(self, id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(id)).fetchone()