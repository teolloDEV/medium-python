#kasus

# - membandingkan 2  buah list
# - tampilkan berapa kali nilai A saat lebih besar dari nilai B

a = [5, 6, 7]
b = [5, 6, 10]

# solusi 1

# def membandingkan_array(a,b):
#     skor_a = 0
#     skor_b = 0
#     for i in range(len(a)):
#         if a[i] > b[i]:
#              skor_a += 1
#         elif a[i] < b[i]:
#              skor_b += 1
#     return skor_b, skor_b

# solusi 2

def membandingkan_array(a, b):

    skor_a = 0
    skor_b = 0
    for x, y in zip(a, b):
        if x > y:
            skor_a += 1
        elif x < y:
            skor_b += 1
    return skor_b, skor_b


print(membandingkan_array(a, b))
