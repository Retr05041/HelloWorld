import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="parker",
  passwd="root"
)

print(mydb)
