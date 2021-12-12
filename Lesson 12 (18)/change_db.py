import sqlite3


DATABASE_NAME = 'school.db'
CLASSES_TABLE = 'classes'
STUDENTS_TABLE = 'students'

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

cursor.execute(f'UPDATE {CLASSES_TABLE} SET id = 1 WHERE id = 5')

connection.commit()
connection.close()