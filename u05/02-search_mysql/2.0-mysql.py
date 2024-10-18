import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="u1",
  password="pwd"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

db_exists=False
for x in mycursor:
  if(x[0]=="student"):
    db_exists=True

if(not db_exists):
    mycursor.execute("CREATE DATABASE student")

mycursor.execute("USE student")

## create the table
table_info="""
create table if not exists STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

mycursor.execute(table_info)

## Insert some more records
mycursor.execute("delete from STUDENT")
mycursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
mycursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
mycursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
mycursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
mycursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

## Display all the records
print("The inserted records are")
mycursor.execute('''Select * from STUDENT''')
for row in mycursor:
    print(row)

## Commit your changes in the database
mydb.commit()
