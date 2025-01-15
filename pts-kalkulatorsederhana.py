# pts-kalkulatorsederhana.py

# Meminta input dua angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Meminta input operator aritmatika dari pengguna
operator = input("Masukkan operator aritmatika (+, -, *, /): ")

# Melakukan operasi sesuai dengan operator yang dimasukkan
if operator == "+":
    hasil = angka1 + angka2
    operasi = "penjumlahan"
elif operator == "-":
    hasil = angka1 - angka2
    operasi = "pengurangan"
elif operator == "*":
    hasil = angka1 * angka2
    operasi = "perkalian"
elif operator == "/":
    if angka2 != 0:  # Memastikan pembagian dengan nol tidak terjadi
        hasil = angka1 / angka2
        operasi = "pembagian"
    else:
        hasil = "Tidak dapat membagi dengan nol!"
        operasi = "pembagian"
else:
    hasil = "Operator tidak valid!"
    operasi = "tidak valid"

# Menampilkan hasil perhitungan
print(f"Hasil {operasi}: {hasil}")