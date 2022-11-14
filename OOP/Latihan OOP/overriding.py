# Penimpaan

class Kendaraan :
    def berjalan(self):
        print('mobil sedang berjalan...')

class Mobil(Kendaraan):
    def berjalan(self):
        print('Berjalan dengan cepat..')

kendaraan1 = Kendaraan()
mobil1 = Mobil()


kendaraan1.berjalan()
mobil1.berjalan()