import random
daftar_khodam = {"khodam harimau" : "penjaga spiritual...."}
def acak_khodam ():
    nama_khodam = random.choice(list(daftar_khodam.keys()))
    deskripsi = daftar_khodam [nama_khodam]
    return f"khodam (import_nama) adalah {nama_khodam}:"
input_nama = input ("masukkan nama kamu : ")
hasil = acak_khodam()
print(hasil)