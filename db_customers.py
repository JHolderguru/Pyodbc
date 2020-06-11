from db_connection_OOP import MSDBconnection


class CustomerTable(MSDBconnection):
    # pass
    def create_entry(self, CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
                     Country, Phone, Fax):
        return self.sql_query(
            f"""INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)
    VALUES (f{CustomerID}, '{CompanyName}', {ContactName}, {ContactTitle},'{Address}', {City}, {Region}, {PostalCode}, {Country}, {Phone}, {Fax})""").commit

    def get_the_id(self, id):
        query_string ="SELECT * FROM Customers WHERE CustomerID = " +"'" + str(id) + "'"
        returning = self.sql_query(query_string)
        return returning

    def get_all(self, customer_name=None):
        result_list = []
        if customer_name is None:
            query_result = self.sql_query('SELECT * FROM Customers')
        else:
            query_result = self.sql_query(f"SELECT * FROM Customers WHERE ContactName LIKE '%{customer_name}%'").commit
        while True:
            row = query_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

    def update_db(self, column_1, val_1, column_2, condition):
        return self.sql_query(f"UPDATE Products SET {column_1} = '{val_1}' WHERE {column_2} = '{condition}'").commit
    #     result_list = []
    #
    # if ContactName == None:
    #     result = self.sql_query('SELECT * FROM Customers')


# Customer = CustomerTable()

# print(Customer.get_the_id('ALFKI'))
# for data in Customer.get_the_id('ANTON'):
#     print(data)

#print(Customer.get_all())


# results = CustomerTable().sql_query('SELECT * FROM Customers')
# while True:
#     row = results.fetchone()
#
#     if row == None:
#          break
#     print(row.ContactName)
