# length - menghitung panjang list
panjanglist = [1, 2, 3, 4]
print ("length", len(panjanglist))

# concatenation - menggabungkan dua list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("concatenation:", combined_list)

# repetition - mengulang elemen list
repetitionlist = ['halo!'] * 4
print("repetition:", repetitionlist)

# membership - memeriksa apakah elemen di dalam list
member = 2 in [1, 2, 3]
print("membership:", member)

# iteration - melakukan iterasi pada list
for x in [1, 2, 3]:
    print(x, end=' ')

# indexing - mengakses elemen berdasarkan indeksnya
L = ['c++', 'java', 'python']
print(L[2])
print(L[-2])

# sicling - mengambil bagian index tertentu
list = ['charger', 'ponsel', 'headphone']
print(list[1:])