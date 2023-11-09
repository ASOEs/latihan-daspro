nilai = []
while True:
    angka = int(input("masukan angka anda : "))
    if angka in nilai:
        print("nilai sudah ada")

    elif angka == 0:
        break
    else:
        nilai.append(angka)

print(nilai)