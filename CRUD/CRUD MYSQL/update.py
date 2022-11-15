import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'phpmyadmin',
    password = 'windows123',
    database = 'latihan_CRUD'
)

cursor = db.cursor()
sql = 'UPDATE customers SET name=%s, address=%s WHERE customers_id=%s'
val = ('arif', 'jepara', 11)

cursor.execute(sql, val)

db.commit()
print('{} data diubah' .format(cursor.rowcount))
