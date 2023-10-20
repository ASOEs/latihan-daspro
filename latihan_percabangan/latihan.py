umur = int(input("masukan umur anda : "))

if umur == 0 :
    print("tidak valid")

elif umur < 18 :
    print("remaja")

elif umur < 65:
    print("dewasa")

else :
    print("anda sudah tua")