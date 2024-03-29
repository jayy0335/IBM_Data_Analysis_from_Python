# import sqlite3
# from databases import Database
from dmodule import connect

#create connection object
connection=connect("databases","users","password")

#create a cursor object
cursor=connection.cursor()

#run queries
cursor.execute('select * from student')
result=cursor.fetchall()

#free resource
cursor.close()
connection.close()