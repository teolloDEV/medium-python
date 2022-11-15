import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'phpmyadmin',
    password = 'windows123',
    database = 'latihan_CRUD'
)

cursor = db.cursor()
sql = 'SELECT * FROM customers'
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)

