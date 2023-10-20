# umur = int(input("masukan umur anda : "))

# if umur == 0 :
#     print("tidak valid")

# elif umur < 18 :
#     print("remaja")

# elif umur < 65:
#     print("dewasa")

# else :
#     print("anda sudah tua")


while True :
    angka = int(input("masukan angka anda : "))
    if angka > 50 and angka % 2 == 1 :
        print("benar")
        break
    else:
        print("masukan angka yang benar")