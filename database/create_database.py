# CREATING DATABASE
# CREATING TABLE
# ADDING DATA TO TABLE BY FORMULA


import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Qwertyu122",
    # !!!!!!!add this row only after you have created the database!!!!!!!!!!
    # database = <database name>
    database="imdb_canada"
)

mycursor = mydb.cursor()

# CREATE DATABASE <name>
mycursor.execute("CREATE DATABASE nameless_db")

# show all databases
mycursor.execute("SHOW DATABASES")

# CREATE TABLE <name> (<column name> <data type>(data maxlength), <column name> <data type>(data maxlength))
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# show all tables
mycursor.execute("SHOW TABLES")


# formula to insert info into table
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
student1 = ("Vlad", 18)
student2 = ("Danylo", 17)
student3 = ("Levon", 17)
student4 = ("Yan", 17)
# mycursor.execute(sqlFormula, student1)
# mycursor.execute(sqlFormula, student2)

stud_lst = [student1, student2, student3, student4]

mycursor.executemany(sqlFormula, stud_lst)
# mydb.commit() ---- use this to actually commit changes to the table
mydb.commit()



# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# mycursor.execute("SHOW TABLES")

# for tb in mycursor:
#     print(tb)

# print(mydb)

