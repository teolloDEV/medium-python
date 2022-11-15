import mysql.connector

db  = mysql.connector.connect(
    host = 'localhost',
    user = 'phpmyadmin',
    password = 'windows123',
    database = 'latihan_CRUD'
)

cursor = db.cursor()
sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
values = [
    ('ar', 'jakarta'),
    ('fsdf', 'isfwe'),
    ('aljfsdf','ioefwwp'),
    ('sdjfjsd','jwhfkl')
]

for val in values:
    cursor.execute(sql, val)
    db.commit()
print('{} data ditambahkan '. format(len(values)))