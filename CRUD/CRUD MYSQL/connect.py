import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='phpmyadmin',
    password='windows123'
)

if db.is_connected():
    print('connected......')