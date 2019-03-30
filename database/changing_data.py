import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Qwertyu122",
    database="imdb_canada"
)

mycursor = mydb.cursor()

# change the value in the table row
# UPDATE <table name> SET <column name> = <your value> WHERE <column name> = <value>
sql = "UPDATE STUDENTS SET age = 19 WHERE name = 'Vlad'"

mycursor.execute(sql)

# mydb.commit()

# get only limited amount of data from the table
# SELECT * FROM <table name> LIMIT <amount of rows>
# mycursor.execute("SELECT * FROM students LIMIT 5")
# myresult = mycursor.fetchall()
#
# for res in myresult:
#     print(res)
#
# print(myresult)

# get limited amount of data starting from a particular element by its number
# SELECT * FROM <table name> LIMIT <amount of rows> OFFSET <how many you want to skip>
mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 3")
myresult = mycursor.fetchall()

for res in myresult:
    print(res)

print(myresult)

