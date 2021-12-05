import sqlite3

#Название базы данных
database_name = 'mydatabase.db'
#Подключение
connection = sqlite3.connect(database_name)
#Курсор
cursor = connection.cursor()
query_create = 'CREATE TABLE IF NOT EXISTS book (author CHAR, year INT)'
cursor.execute(query_create)
#Создание записи в таблице
query_select = 'SELECT * FROM book'
cursor.execute(query_select)
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()

