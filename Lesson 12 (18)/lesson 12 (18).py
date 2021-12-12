import sqlite3


DATABASE_NAME = 'school.db'
CLASSES_TABLE = 'classes'
STUDENTS_TABLE = 'students'
SUBJECTS = 'subjects'
MARKS = 'marks'
DROP_COMMAND = 'DROP TABLE IF EXISTS '

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

cursor.execute(DROP_COMMAND + CLASSES_TABLE)
cursor.execute(DROP_COMMAND + STUDENTS_TABLE)
cursor.execute(DROP_COMMAND + SUBJECTS)
cursor.execute(DROP_COMMAND + MARKS)

cursor.execute('PRAGMA foreign_keys=on')

cursor.execute(f'CREATE TABLE IF NOT EXISTS {CLASSES_TABLE} (id INT NOT NULL \
                PRIMARY KEY, class CHAR(3), num_of_stud INT(2), teacher CHAR)')

cursor.execute(f'CREATE TABLE IF NOT EXISTS {STUDENTS_TABLE} (id INT NOT NULL \
                PRIMARY KEY, surname CHAR, name CHAR, second_name CHAR, id_classes \
                INT NOT NULL, age INT(2), FOREIGN KEY (id_classes) REFERENCES \
                classes (id) ON UPDATE CASCADE)')

cursor.execute(f'CREATE TABLE IF NOT EXISTS {SUBJECTS} (id INT NOT NULL \
                PRIMARY KEY, subject CHAR)')

cursor.execute(f'CREATE TABLE IF NOT EXISTS {MARKS} (id INT NOT NULL \
                PRIMARY KEY, mark INT(2), id_students INT NOT NULL, \
                id_subjects INT NOT NULL, FOREIGN KEY (id_students) REFERENCES \
                students (id) ON UPDATE CASCADE, FOREIGN KEY (id_subjects) REFERENCES \
                subjects (id) ON UPDATE CASCADE)')

connection.commit()
connection.close()
