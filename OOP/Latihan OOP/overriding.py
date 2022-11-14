# Penimpaan

class Kendaraan :
    def berjalan(self):
        print('mobil sedang berjalan...')

class Mobil(Kendaraan):
    pass

kendaraan1 = Kendaraan()
mobil1 = Mobil()


kendaraan1.berjalan()
mobil1.berjalan()