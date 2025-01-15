import phonenumbers
from phonenumbers import carrier, geocoder, timezone

notelp = input("masukkan nomor: ")
notelp = phonenumbers.parse(notelp, "ID")

# get loc
print(timezone.time_zones_for_number(notelp))

# get provider
print(carrier.name_for_number(notelp, "en"))

# get city
print(geocoder.description_for_number(notelp, "en"))

# validasi nomor
print("validasi nomor telepon: ", phonenumbers.is_valid_number(notelp))

# cek kemungkinan nomor
print("cek kemungkinan nomor: ", phonenumbers.is_possible_number(notelp))