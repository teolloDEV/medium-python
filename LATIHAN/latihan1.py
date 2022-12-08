

ar = [1,2,3,4,10,11]

# solusi 1
# def simple_array_sum(ar):
#     hasil_jumlah = 0
#     for i in range(len(ar)):
#         hasil_jumlah += ar[i]
#     return hasil_jumlah


#solusi 2

# def simple_array_sum(ar):
#     hasil = 0
#
#     for bil in ar:
#         hasil += bil
#     return hasil

# solusi 3

def simple_array_sum(ar):
    return sum(ar)


print(simple_array_sum(ar))


