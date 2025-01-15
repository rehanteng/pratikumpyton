# IF CONDITION
# nilai = 85 
#nilai = int(input("masukan nilai santri : "))
#if nilai >= 80:
 #   print("anda lulus dengan nilai yang baik")
#else:
 #   print("tingkatkan belajarnya")    


#umur = 18 
#umur = int(input("masukan umur anda : "))
#if umur >= 20:
 #   print("anda dapat membuat sim dengan baik")
#else:
 #   print("anda tidak dapat membuat sim dengan baik")

 
nilai = int(input("masukan nilai santri : "))
if nilai >= 90:
    print("grade A :")
elif nilai >= 80:
    print("grade B+")
elif nilai >= 70:
    print("grade B")
elif nilai >= 60:
    print("grade C+")
elif nilai >= 50:
    print("grade C")
elif nilai >= 40:
    print("grade D")
else:
    print("Grade E")