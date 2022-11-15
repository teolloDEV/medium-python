buku = []

def tampil():
    index = 0
    if len(buku) <= 0:
        print('data masih kosong')
    else:
        for book in buku:
            print(str(index) + ' - ' + book + '\n\n')
            index = index + 1
def tambah ():
    judul = input('Masukkan judul buku : ')
    buku.append(judul)
    print('Data sudah di tambahkan ')


def edit():
    tampil()
    index = int(input('Masukkan nomor berapa data yang akan diedit : '))
    judul_lama = buku[index]
    judul_baru = input('Masukkan judul baru : ')
    buku[index] = judul_baru
    print(judul_lama + 'telah diperbarui menjadi '+ judul_baru)

def hapus():
    tampil()
    index = int(input('Masukkan nomor berapa data yang akan diedit : '))
    judul_lama = buku[index]
    del buku[index]
    print(judul_lama + 'Telah dihapus')


def menu():
    print('1 - tampil')
    print('2 - tambah')
    print('3 - edit')
    print('4 - hapus')


    kode = input('Masukkan kode : ')
    if kode == '1':
        tampil()
    elif kode == '2':
        tambah()
    elif kode == '3':
        edit()
    elif kode == '4':
        hapus()
    else:
        print('kode salah')
while(True):
    menu()
