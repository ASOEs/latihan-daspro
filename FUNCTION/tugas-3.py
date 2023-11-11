def hitung_total(*args):
    total = sum(args)
    rata_rata = total / len(args)
    return total,rata_rata

angka = input("masukan angka anda : ")
nilai_list = [int(nilai) for nilai in angka.split(",")]

total, rata_rata = hitung_total(*nilai_list)
print(f"total : {total}")
print(f"rata rata : {rata_rata}")



