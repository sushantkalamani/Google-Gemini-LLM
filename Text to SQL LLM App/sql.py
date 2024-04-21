import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = '''
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
'''

cursor.execute(table_info)

cursor. execute('''Insert Into STUDENT values('Sushant', 'Data Science','A', 85)''')
cursor.execute('''Insert Into STUDENT values('Amit', 'Electronics', 'A', 100)''')
cursor.execute('''Insert Into STUDENT values('Nikhil', 'Web Development', 'B', 70)''')
cursor.execute('''Insert Into STUDENT values('Ritesh', 'DEVOPS', 'A', 50)''')
cursor.execute('''Insert Into STUDENT values('Rajeev', 'Data Science', 'A', 65)''')
cursor.execute('''Insert Into STUDENT values('Chetan', 'DEVOPS', 'A', 35)''')

print("The inserted records are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()