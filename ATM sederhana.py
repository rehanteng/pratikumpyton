# atmpython
print("     SELAMAT DATANG DI MESIN ATM")
print("======================================")
print("PILIH TRANSAKSI YANG ANDA INGINKAN :")
print("1. INFORMASI SALDO")
print("2. PENARIKAN TUNAI")
print("3. SETOR TUNAI")
print("4. TRANSFER TUNAI")
print("5. TAMPILKAN MENU TRANSAKSI")
print("0. KELUAR")

saldo = 0

while True:
    pilih_menu = int(input("MASUKKAN MENU YANG ANDA PILIH :"))
    
    if pilih_menu == 0:
        break

    elif pilih_menu == 1:
        print(f"SALDO ANDA SAAT INI ADALAH Rp {saldo}")
        print("SILAHKAN PILIH MENU LAIN")
        print("======================================")

    elif pilih_menu == 2:
        print("MASUKKAN NOMINAL YANG INGIN ANDA TARIK")
        jumlah_ditarik = int(input("Rp "))
        if jumlah_ditarik < saldo:
            saldo -= jumlah_ditarik
            print("PENARIKAN YANG ANDA LAKUKAN SUDAH BERHASIL")
            print(f"SISA SALDO ANDA SAAT INI ADALAH Rp {saldo}")
            print("SILAHKAN AMBIL UANG ANDA DAN PILIH MENU LAIN")
            print("======================================")
        else:
            print("SALDO ANDA TIDAK CUKUP UNTUK MELAKUKAN PENARIKAN INI")
            print("SILAHKAN MASUKKAN NOMINAL LAIN ATAU PILIH MENU LAIN")
            print("======================================")

    elif pilih_menu == 3 :
        print("MASUKKAN NOMINAL YANG INGIN ANDA SETOR")
        jumlah_disetor = int(input("Rp "))
        saldo += jumlah_disetor
        print("UANG YANG ANDA SETOR SUDAH DITAMBAHKAN KE SALDO ANDA")
        a = input("APAKAH ANDA INGIN MELIHAT SALDO SAAT INI (y/n)? :")
        if a == "y" :
            print(f"Saldo Anda saat ini adalah Rp {saldo}")
            print("SILAHKAN PILIH MENU LAIN")
            print("======================================")
        elif a== "n" :
            print("======================================")
        else:
            print("SISTEM ERROR")
            print("======================================")

    elif pilih_menu == 4:
        rekening_tujuan = input("MASUKKAN NO REKENING TUJUAN ANDA : ")
        nominal_transef = int(input("MASUKKAN NOMINAL YANG INGIN ANDA TRANSFER : Rp "))
        if nominal_transef < saldo:
            saldo -= nominal_transef
            print(f"ANDA AKAN MELAKUKAN TRANSFER KE NO REKENING {rekening_tujuan[0:5]}XXXXXX")
            print(f"SEBESAR RP {nominal_transef}")
            print("TRANSFER UANG YANG ANDA LAKUKAN SUDAH BERHASIL")
            print(f"SISA SALDO ANDA SAAT INI ADALAH Rp {saldo}")
            print("SILAHKAN PILIH MENU LAIN")
            print("======================================")
        else:
            print("SALDO ANDA TIDAK CUKUP UNTUK MELAKUKAN TRANSFER TUNAI")
            print("SILAHKAN MASUKKAN NOMINAL LAIN ATAU PILIH MENU LAIN")
            print("======================================")
            
    elif pilih_menu == 5:
        print("1. INFORMASI SALDO")
        print("2. PENARIKAN TUNAI")
        print("3. SETOR TUNAI")
        print("4. TRANFER TUNAI")
        print("5. TAMPILKAN MENU TRANSAKSI")
        print("0. KELUAR")
        print("======================================")
    else:
        print("MENU YANG ANDA PILIH SALAH, SILAHKAN MASUKKAN MENU YANG BENAR")