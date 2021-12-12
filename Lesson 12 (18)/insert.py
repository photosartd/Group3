import sqlite3


DATABASE_NAME = 'school.db'
CLASSES_TABLE = 'classes'
STUDENTS_TABLE = 'students'

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

classes = (
    (1, '7А', 30, 'Иванов Иван Иванович'),
    (2, '10Б', 25, 'Сидоров Сидр Сидорович'),
    (3, '9В', 20, 'Васечкин Василий Васильевич')
)

for each in classes:
    cursor.execute(f'INSERT INTO {CLASSES_TABLE} VALUES(?, ?, ?, ?)', each)

students = (
    (1, 'Смирнов', 'Федор', 'Дмитриевич', 2, 13),
    (2, 'Ефремов', 'Иван', 'Николаевич', 1, 14),
)
for each in students:
    cursor.execute(f'INSERT INTO {STUDENTS_TABLE} VALUES(?, ?, ?, ?, ?, ?)', each)

connection.commit()
connection.close()