from db_connection_OOP import MSDBconnection


class CustomerTable(MSDBconnection):
    def create_entry(self, CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
                     Country, Phone, Fax):
        return self.sql_query(
            f"""INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)
    VALUES (f{CustomerID}, '{CompanyName}', {ContactName}, {ContactTitle},'{Address}', {City}, {Region}, {PostalCode}, {Country}, {Phone}, {Fax})""")

    def get_the_id(self, id):
        return self.sql_query('SELECT * FROM Customers WHERE CustomersID=' + str(id)).fetchone()

    def get_all_customers(self, ContactName =None):
        result_list = []

        if ContactName == None:
            q_result = self.sql_query('SELECT * FROM Customers')
