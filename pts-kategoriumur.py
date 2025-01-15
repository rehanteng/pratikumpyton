# pts-kategoriumur.py

# Meminta input umur dari pengguna
umur = int(input("Masukkan umur: "))

# Menentukan kategori usia berdasarkan umur
if umur < 12:
    kategori = "Anak-anak"
elif 12 <= umur <= 17:
    kategori = "Remaja"
elif 18 <= umur <= 64:
    kategori = "Dewasa"
elif umur >= 65:
    kategori = "Tua"
else:
    kategori = "Kategori tidak valid"

# Menampilkan kategori usia
print(f"Kategori: {kategori}")