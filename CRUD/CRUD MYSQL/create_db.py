import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'phpmyadmin',
    password = 'windows123',
    database = 'latihan_CRUD'
)

#Membuat DATABASE
cursor = db.cursor()
cursor.execute('CREATE DATABASE latihan_CRUD')

print('Database berhasil dibuat')