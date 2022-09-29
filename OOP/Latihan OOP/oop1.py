class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def get_luas(self):
        return 0.5 * self.alas * self.tinggi

segitiga1 = segitiga(20,45)


print('Luas segitiga 1 adalah : ', segitiga1.get_luas())