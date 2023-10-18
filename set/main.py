# pembelajaran kuliah mengenai set
# set menggunakan tanda kurung kurwl {}
# set bersifat unordered
# contoh 
a = {"apel", "jeruk", "strawberry", "durian"}
print(f"ini adalah contoh data set : {a}")

print("=====cara mengetahui panjang set=====")
# cara mengetahui panjang data set yaitu dengan :
print(len(a))

print("=====***=====")
# karna set tidak memiliki index maka jika ingin mengambil data yang ada 
# dalam set yaitu dengan cara :
a = {"apel", "jeruk", "strawberry", "durian"}
for item in a :
    print(item)

print("=====***=====")
# cara menambahkan item di set
a.add("mangga")
print(f"ini adalah data yang sudah di tambah : \n {a}")

# cara mengabungkan set dengan set lainnya
a = {"apel", "jeruk", "strawberry", "durian"}
b = {"ikan", "lauk", "buah"}
c = a.union(b)
print(f"ini adalah data yang telah di gabungkan :\n {c}")


a = {"apel", "jeruk", "strawberry", "durian"}
a.pop()
print(f"ini adalah data yang telah di hapus : {a}")

# cara menghapus semua set 
a = {"apel", "jeruk", "strawberry", "durian"}
a.clear()
print(a)



