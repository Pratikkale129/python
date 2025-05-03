import my_sql_connector as myconn
mydb = myconn.connect(host = 'localhost', user = 'root', password = 'Escort@2024', database='escortcoder')
print(mydb,"Connected Databses Successfuly")