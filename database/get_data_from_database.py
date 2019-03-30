# SELECTING ALL DATA OR SPECIFIC COLUMN DATA FROM DATABASE
# GETTING THAT DATA


import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Qwertyu122",
    database="imdb_canada"
)

mycursor = mydb.cursor()

# to select all columns from table
# SELECT * FROM <table name>
mycursor.execute("SELECT * FROM students")

# to select the data only from specified column
# SELECT <column name> FROM <table name>
mycursor.execute("SELECT age FROM students")

# gets all data from last execute statement
myresult = mycursor.fetchall()

# gets only the first result from execute statement
myresult = mycursor.fetchone()

for row in myresult:
    print(row)
