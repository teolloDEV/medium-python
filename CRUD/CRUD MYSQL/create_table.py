import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'phpmyadmin',
    password = 'windows123',
    database = 'latihan_CRUD'
)

cursor = db.cursor()

sql = ''' CREATE TABLE customers (
    customers_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR (255),
    address VARCHAR(255)
)

'''

cursor.execute(sql)
print('table customers berhasil dibuat')
