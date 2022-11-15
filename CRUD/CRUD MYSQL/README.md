## Tutorial Python dan MySQL: Membuat Aplikasi CRUDS Berbasis Teks

### Instalasi Modul MySQL Connector


    sudo apt install python3-mysql.connector


atau bisa juga menggunakan pip:

    pip3 install mysql-connector

> - Pertama-tama kita membutuhkan modul mysql.connector untuk membuat koneksi ke MySQL.
> - Kemudian kita membuat koneksi dengan memanggil fungsi connect() dan parameter host, user, dan passwd.
> - Sebenarnya ada satu lagi parameter, yaitu database untuk menentukan nama database yang akan digunakan. 
### Percobaan Koneksi ke MySQL

```commandline
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin"
)

if db.is_connected():
  print("Berhasil terhubung ke database")
  ```

lalu panggil dengan

    python3 connect.py