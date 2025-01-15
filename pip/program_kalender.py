print("|===============================|")
print("|   PROGRAM MENAMPILKAN KALENDER   |")
print("|===============================|")

import calendar

tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan Bulan: "))
print()

print("Hasil")
print(calendar.month(tahun, bulan))