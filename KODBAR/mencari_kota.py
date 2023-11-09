kota = ["jakarta", "bandung", "cirebon", "indramayu", "bogor"]
kotaYangDicari = input("kota yang di cari : ")

i = 0
while i < len(kota):
    if kota[i] == kotaYangDicari:
        print(f"kota ada")
        break

    print(f"bukan {kota[i]}")
    i += 1
else:
    print("kota tidak ada di dalam daftar")
