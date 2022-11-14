
#PUBLIC

# class Segitiga:
#
#   def __init__(self, alas, tinggi):
#     self.alas = alas
#     self.tinggi = tinggi
#     self.luas = 0.5 * alas * tinggi
#
# segitiga_besar = Segitiga(100, 80)
#
# # akses variabel alas, tinggi, dan luas dari luar kelas
# print(f'alas: {segitiga_besar.alas}')
# print(f'tinggi: {segitiga_besar.tinggi}')
# print(f'luas: {segitiga_besar.luas}')

# Protected Access Modifier

# class Mobil:
#   def __init__(self, merk):
#     self._merk = merk
#
# sedan = Mobil('Toyota')
#
# # tampilkan _merk dari luar kelas
# print(f'Merk: {sedan._merk}')

# class Mobil:
#   def __init__(self, merk):
#     self._merk = merk
#
# class MobilBalap(Mobil):
#   def __init__(self, merk, total_gear):
#     super().__init__(merk)
#     self._total_gear = total_gear
#
#   def pamer(self):
#     # akses _merk dari subclass
#     print(
#       f'Ini mobil {self._merk} dengan total gear {self._total_gear}'
#     )
#
# ferrari = MobilBalap('Ferrari', 8)
# ferrari.pamer()

# Private Access Modifier

# class Mobil:
#   def __init__(self, merk):
#     self.__merk = merk
#
# jip = Mobil('Jeep')
# print(f'Merk: {jip.__merk}')

# kode di atasa akan error

# class Mobil:
#   def __init__(self, merk):
#     self.__merk = merk
#
#   def tampilkan_merk(self):
#     print(f'Merk: {self.__merk}')
#
# jip = Mobil('Jeep')
# jip.tampilkan_merk()

# Accessor Mutator

