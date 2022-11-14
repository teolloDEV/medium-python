# Membuat object induk

class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f'Hello perkenalkan nama saya {self.nama}, dan saya berasal dari {self.asal}')


# Object turunan (Child)

class Pelajar(Orang):
    pass
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal


class Pekerja(Orang):
    pass
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal


# Memanggil object Induk

arif = Orang('arif', 'jepara')
arif.perkenalan()

# Memanggil Object turunan (Child)

roy = Pelajar('roy','bandung')
roy.perkenalan()
alex = Pekerja('alex', 'Jakarta')
alex.perkenalan()






#Membuat Konstruktor pada kelas turunan
class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
    print('fungsi orang __init__ telah diekskusi')