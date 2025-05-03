import mysql.connector as myconn
mydb = myconn.connect(host = 'localhost', user = 'root', password = 'Escort@2024', database='escortcoder')
print(mydb,"Connected Databses Successfuly")
db_cursor = mydb.cursor() # MySql Data Accessing of Database
db_cursor.execute('create database CodeBlockAcademy')
