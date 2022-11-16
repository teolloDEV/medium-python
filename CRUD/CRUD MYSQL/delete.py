import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'phpmyadmin',
    password = 'windows123',
    database = 'latihan_CRUD'
)

cursor = db.cursor()
sql = 'DELETE FROM customers WHERE customers_id = %s'
val = (11, )
cursor.execute(sql, val)

db.commit()

print('{} data dihapus ' .format(cursor.rowcount))