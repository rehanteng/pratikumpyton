# length - menghitung panjang tuple
panjangtup = (1, 2, 3, 4)
print ("length:", len(panjangtup))

# concatenation - menggabungkan dua tuple
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
combined_tup = tup1 + tup2
print("concatenation:", combined_tup)

# repetition - mengulang elemen tuple
repetitiontup = ('halo!') * 4
print("repetition:", repetitiontup)

# membership - memeriksa apakah elemen di dalam tuple
member = 2 in (1, 2, 3)
print("membership:", member)

# iteration - melakukan iterasi pada tuple
for x in (1, 2, 3):
    print(x, end=' ')

# indexing - mengakses elemen berdasarkan indeksnya
T = ('c++', 'java', 'python')
print(T[2]) 
print(T[-2])

# sicling - mengambil bagian index tertentu
tuple = ('charger', 'ponsel', 'headphone')
print(tuple[1:])