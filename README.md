#PYODBC and OOP
We are looking into the PYODBC package.

1.And we are going to use the package to make a OOP module that abstracts our interaction with the NW DB. Starting with the connection.

2.And then further abstract the interaction with specific Tables.

3.Finally, where appropriate we will use the CRUD desing to build methods.

##CRUD
###CREATE
still updating this for now 


###READ

### READ one

### READ all

### Update

### Destroy

### Delete

### Example documentation
This repo's is for the abstraction of the NW db with PYODBC.

Please read bellow for the available method for each table

Product table
you can CRUD the product table. Avialble methods:

Initialisation
    products_table_instance = DBProduct_table()
get_by_id(self, id) --> one object
use this method to get out a product by ID

example

    '''python 
    instance.get_by_id(15) 
    #-> row with product id = 15'''