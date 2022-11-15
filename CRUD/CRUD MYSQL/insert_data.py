import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'phpmyadmin',
    password = 'windows123',
    database = 'latihan_CRUD'
)

cursor = db.cursor()
sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
val = ('arif', 'jepara')

cursor.execute(sql, val)
db.commit()

print('{} - Data ditambahkan ' .format(cursor.rowcount))