# class Mahasiswa:
#     nama = None
#     alamat = None
#     pekerjaan = None
#
#
#     def perkenalan(self):
#         print(f'hallo perkenalkan nama saya {self.nama} saya dari {self.alamat} dan saya bekerja sebagai {self.pekerjaan}')
#
# mahasiswa1 = Mahasiswa()
# mahasiswa1.nama = 'arif'
# mahasiswa1.alamat = 'jepara'
# mahasiswa1.pekerjaan = 'programmer'
#
# mahasiswa1.perkenalan()

# Contoh penggunaan Konstruktor

# class Mahasiswa:
#     def __init__(self, nama, asal, aktifitas):
#         self.nama = nama
#         self.asal = asal
#         self.aktifitas = aktifitas
#
#     def perkenalan(self):
#         print(f'perkenalkan nama saya {self.nama} saya berasal dari {self.asal}')
#         print(f'aktifitas saya sekarang adalah sebagai {self.aktifitas}')
#
# mahasiswa1 = Mahasiswa('arif', 'jepara','programmer')
# mahasiswa1.perkenalan()


class Mobil:
    def __init__(self, warna, merek):
        self.warna = warna
        self.merek = merek

class Mahasiswa:
    def __init__(self, nama, asal, mobil):
        self.nama = nama
        self.asal = asal
        self.mobil = mobil


    def perkenalan(self):
        print(f'hallo perkenalkan nama saya {self.nama}, saya berasal dari kota {self.asal}')
        print(f'saya mempunyai mobil berwarna {self.mobil.warna}, dengan merek {self.mobil.merek}')


mahasiswa1 = Mahasiswa (
    nama = 'Arif',
    asal = 'Jepara',
    mobil = Mobil(
        warna ='Merah',
        merek = 'BMW'
    )
)

mahasiswa1.perkenalan()