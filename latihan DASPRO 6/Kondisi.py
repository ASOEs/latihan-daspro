nilai = float(input("masukan nilai anda : "))
kondisi = float(input("masukan kondisi keuangan anda : "))

if (nilai > 90) and (kondisi < 2000000) :
    print("selamat anda mendapatkan beasiswa PENUH")

elif (nilai > 80 <= 90) and (kondisi > 4000000) :
    print("Selamat anda mendapatkan beasiswa PARSIAL")

else :
    print("Anda tidak mendapat beasiswa")