class Segitiga :
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def get_luas(self):
        return 0.5 * self.alas * self.tinggi

segitiga1 = Segitiga(13, 4)
segitiga2 = Segitiga(24,55)

print('luas segitiga1:', segitiga1.get_luas())
print('luas segitiga2:', segitiga2.get_luas())