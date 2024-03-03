import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("EMPLOYEE.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table COSTA_EMPLOYEE(NAME VARCHAR(25),DESIGNATION VARCHAR(25),
DEPARTMENT VARCHAR(25),SALARY INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into COSTA_EMPLOYEE values('ASHUTOSH','SOFTWARE ENGINEER','NLP',22000)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('RUPA','SOFTWARE ENGINEER','NLP',25000)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('NAVEEN','SOFTWARE ENGINEER','MACHINE LEARNING',25000)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('AMIT','SENIOR SOFTWARE ENGINEER','COMPUTER VISION',25000)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('ARIZ','SOFTWARE ENGINEER','DATA ANALYTICS',25000)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('ANKIT','JUNIOR ENGINEER','DATA ANALYTICS',26500)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('SANDEEP','SOFTWARE ENGINEER','MACHINE LEARNING',25000)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('MANSI','INTERN','NLP',0)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('KHUSHI','INTERN','NLP',0)''')
cursor.execute('''Insert Into COSTA_EMPLOYEE values('DEEPIKA','HR','RECRUITER',33000)''')

## Disspaly ALl the records

print("The inserted  records are")
data=cursor.execute('''Select * from COSTA_EMPLOYEE''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
