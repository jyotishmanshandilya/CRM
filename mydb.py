import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Johnny#2003'
)

# prepare a cursor
cursorObject = database.cursor()

# create a database
cursorObject.execute('create database crmdb')

print("Database created!")