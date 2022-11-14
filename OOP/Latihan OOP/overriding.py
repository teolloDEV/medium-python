# class Kendaraan:
#     def berjalan(self):
#         print('berjalan >>>')
# class Mobil(Kendaraan):
#     pass
#
# honda = Kendaraan()
# BMW = Mobil()
#
# honda.berjalan()
# BMW.berjalan()

# Proses overriding
#
# class Kendaraan:
#     def berjalan(self):
#         print('berjalan...')
#
# class Mobil(Kendaraan):
#     def berjalan(self):
#         print('Mobil melaju dengan kencang')
#
#
# motor = Kendaraan()
# bmw = Mobil()
# motor.berjalan()
# bmw.berjalan()

# Menambah parameter pada fungsi yg di timpa
# Mobil akan ditambah dengan kecepatan dan satuan kecepatan

# class Kendaraan:
#     def berjalan(self):
#         print('berjalan...')
#
# class Mobil(Kendaraan):
#     def berjalan(self, kecepatan, satuan =  'km/jam'):
#         print(f'Mobil melaju dengan kecepatan {kecepatan} {satuan}')
#
#
# motor = Kendaraan()
# bmw = Mobil()
# motor.berjalan()
# bmw.berjalan(200)

# memanggil fungsi pada kelas induk

class Kendaraan:
    def berjalan(self):
        print('berjalan...')

class Mobil(Kendaraan):
    def berjalan(self, kecepatan, satuan =  'km/jam'):
        super().berjalan()
        print(f'--->>> Mobil melaju dengan kecepatan {kecepatan} {satuan}')


motor = Kendaraan()
bmw = Mobil()
motor.berjalan()
bmw.berjalan(200)