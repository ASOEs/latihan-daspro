# oprasi / manipulasi data list
orang = ["achmad", "soe", "wardi", "asoe"]
# cara mengambil data dari list 
orangPertama = orang[0]
print(f"orang pertama dalam index 0 adalah : {orangPertama}")

panjang_data = len(orang)
print(f"panjang datanya adalah : {panjang_data}")

# cara menambahkan list
# orang.insert(index,item)
orang.insert(0,"asu")
print(f"data yang sudah di tambahkan : {orang}")

# orang.append untuk menambahkan di akhir
orang.append("jajang")
print(f"data yang telah di update : {orang}")

# cara menambahkan list dengan list atau data gabungan
orang_baru = ["agus", "ugas", "suga"]
orang.extend(orang_baru)
print(f"ini adalah list yang di tambah list : {orang}")

# merubah data 
orang[0] = "anj"
print(orang)

# remove data
orang.remove("anj")
print(f"data remove : {orang}")

# data pop data ahir
data_akhir = orang.pop()
print(data_akhir)