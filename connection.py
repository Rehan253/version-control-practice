import mysql.connector as Myconn

mydb = Myconn.connect(
    host="localhost",
    user="root",  # Replace with your actual username
    password=""  # Replace with your actual password
)

if(mydb):
    print("Connection Successful!")
else:
    print("Connection unsuccessful!")

