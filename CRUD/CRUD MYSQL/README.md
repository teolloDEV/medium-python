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

### Membuat Database

> - Selain objek db, kita membutuhkan satu lagi objek yaitu cursor untuk mengeksekusi perintah SQL atau query. Objek ini berada di dalam objek db.

Sehingga untuk membuat objek cursor kita tinggal buat seperti ini

    cursor = db.cursor()

> - Lalu untuk mengeksekusi query, tinggal panggil method execute() dengan parameter string query.

    cursor.execute(sql)
### Membuat Tabel
> - Cara membuat tabel sama seperti cara membuat database. Kita tinggal masukan perintah SQL atau query ke dalam method execute().

```commandline
db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="toko_mainan"
)
```

### Insert Data

```commandline
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="toko_mainan"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Dian", "Mataram")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
```

> - Pada kode tersebut kita menggunakan %s sebagai placeholder untuk value atau data yang akan kita tambahkan.


Mengapa tidak menggunakan seperti ini saja:

```commandline
name = "Dian"
address = "Mataram"
sql = "INSERT INTO customers (name, address) VALUES ('"+ name +"', '" + address +"')"
```

> - Ini kurang aman, karena bisa terkena SQL injection dan juga kurang rapi.

Terakhir kita harus lakukan **db.commit()** untuk menyimpan data. Method ini biasanya dipanggil saat insert data, update data, dan hapus data.

### Menampilkan Data
> Kita dapat menampilkan data dari MySQL dengan query SELECT. Kemudian kita ambil datanya dengan method:

> - ***fetchall()*** untuk ambil semua data;
> - ***fetachmany(10)*** untuk ambil 10 data;
> - ***fetchone()*** untuk mengambil satu data pertama saja.


### UPDATE Data

> - Caranya sama seperti insert data. 
> - Bedanya, kalau update kita harus menggunakan query UPDATE.

```commandline
cursor = db.cursor()
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
val = ("Ardianta", "Lombok", 1)
cursor.execute(sql, val)
```


