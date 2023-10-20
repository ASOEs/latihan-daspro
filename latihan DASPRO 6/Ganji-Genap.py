Angka = input("masukan angka  : ")

if Angka.isnumeric() :
    nilai = int(Angka)

    if nilai %2 == 0 :
        print(f"angka ini {Angka} merupakan genap")

    else :
        print(f"angka ini {Angka} merupakan ganjil")

else :
    print("maaf masukan nilai angka")