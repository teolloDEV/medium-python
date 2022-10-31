def masukkan_alas_dan_tinggi ():
    alas = float(input('Masukkan Alas : '))
    tinggi = float(input('Masukkan Tinggi :'))

    return alas, tinggi

def hitung_luas (alas, tinggi):
    return 0.5 * alas * tinggi

#dalam fungsionaal kita sendiri yang mengelola hasilnya kembali

# satu fungsi bisa dipanggil secara independent

print(hitung_luas(5, 10))
# contoh dengan inputan
alas, tinggi = masukkan_alas_dan_tinggi()
print(hitung_luas(alas, tinggi))