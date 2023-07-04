import mysql.connector as Myconn
mydb = Myconn.connect(
    host="localhost",
    user="root",  
    password="" , 
    database = "mydb1"
)

dbcursor = mydb.cursor()
#dbcursor.execute("Create database mydb1")
#print("Database Created!")

# Execute query to fetch databases
dbcursor.execute("SHOW DATABASES")

# print all databases
for db in dbcursor:
    print(db)

# Crate Table
#dbcursor.execute("CREATE TABLE EMPLOYEE (Name varchar(30), Salary int(20), email varchar(40))")

dbcursor.execute("SHOW TABLES")

for tb in dbcursor:
    print("Table: ",tb)

# insert values into table

query = "INSERT INTO EMPLOYEE (Name,Salary) VALUES (%s,%s)"
Employee = [("Ali",50000),("Waseef",20000),("Hassan",40000)]

dbcursor.executemany(query,Employee)
print("Values Inserted!")

# Read Values from Employee Table
dbcursor.execute("SELECT * FROM EMPLOYEE")  # Modify table name to "EMPLOYEE"

# Fetch all rows from the result
result = dbcursor.fetchall()

# Iterate over the rows and print the values
for row in result:
    print(row)

