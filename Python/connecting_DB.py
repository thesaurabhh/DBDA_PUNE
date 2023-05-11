# Example 1 : 
# Oracle connection from Python
# pip install cx_Oracle

import cx_Oracle

# Establish the database connection
"""The connect() method is passed the username, the password and the connection string 
It consists of the hostname of your machine, localhost, and the database service name orclpdb1. (In Python Database API terminology, the connection string parameter is called the "data source name", or "dsn".)"""

connection = cx_Oracle.connect(user="your_username", password="your_password",dsn="@HOST:PORT/service_name")

# Obtain a cursor
cursor = connection.cursor()

# Data for binding if any for the Query
manager_id = 145
first_name = "Peter"

# Execute the query
sql = """SELECT :mid,:fn  FROM dual """
cursor.execute(sql, mid=manager_id, fn=first_name)

# Loop over the result set
for row in cursor:
    print(row)
    
    
# Example 2:     
    
""" MYSQL Connection from Python"""    
# pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "yourusername",
	password = "your_password"
)

# Obtain a cursor
cursor = mydb.cursor()

# Data for binding if any for the Query
manager_id = 145
first_name = "Peter"

# Execute the query
sql = """SELECT :mid,:fn """
cursor.execute(sql, mid=manager_id, fn=first_name)

# Loop over the result set
for row in cursor:
    print(row)



# Example 3 : Mongodb
# pip install pymongo

# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://host:port/")
database = client["LMS"]
collection = database["LMS_MEMBERS"]

cursor = collection.find({})

for doc in cursor:
    print(doc)

client.close()
