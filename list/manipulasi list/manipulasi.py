## oprasi pada list / manipulasi pada list
data = ["ahmad", "soe", "ardi"]
# memanggil data dari list di atas
# index bisa di mulai dari (0,1,2,3,4 dst) atau bisa juga lewat bilangan bulat (-1,-2,-3,-4 dst)
# jika index diambil dari angka bulat (-) itu akan mengambil dari yang paling depan 
# contoh mengambil lewat bilangan asli 
data_0 = data[0]
print(f"ini contoh pengambilan index dari bilangan asli (index 0) : {data_0}")

# contoh pengambilan data menggunakan bilangan bulat
data_1 = data[-1]
print(f"ini contog pengambilan data dari bilangan bulat (index -1) : {data_1}")

# mengambil info panjang data dari list
info_data = len(data)
print(f"ini adalah panjang data dari (data) : {info_data}")

print("=====LIST MANIPULASI=====")
## manipulasi data list
# menambahkan data list pada tempat yang di inginkan
print(f"ini adalah data sebelum di rumah : {data}")
data.insert(1, "asoe")
# data.insert(index, "nilai yang mau dirubah jadi apa")
print(f"data yang sudah di rubah : \n {data}")

# menambahkan data di akhir
data.append("adut")
print(f"ini data yang sudah di update kembali : \n {data}")

# cara menambah list dengan list 
data_tambahan = ["asep","jajang","ucup"]
data.extend(data_tambahan)
print(f"ini adalah data list yang telah di tambahkan dengan list baru : \n {data}")

# merubah data 
# merubah data dengan index yang di pilih sama kita
# contoh kita ingin menambah data di index ke 2 dengan usep
data[2] = "usep"
print(f"ini adalah data yang telah di tambahkan : \n {data}")

# cara meremove data yang ingin kita pilih
data.remove("usep")
print(f"ini data yang telah di hapus : \n {data}")

# cara menghapus data paling akhir 
data.pop()
print(f"ini adalah data yang telah di hapus : \n {data}")