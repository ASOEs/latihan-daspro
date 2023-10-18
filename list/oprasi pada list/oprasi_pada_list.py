# kita punya data angka random
data = [1,2,2,3,4,1,2,5,4]
print(f"ini adalah data yang kita punya : \n {data}")

# count data atau seberapa banyak angka tersebut muncul atau bisa di sebut modulus
print(f"=====COUNT DATA=====")
jumlah_data_2 = data.count(2) #ini adalah cara atau sintaks ingin mencari tahu seberapa banyak angka 2 dalam data diatas
jumlah_data_4 = data.count(4)
jumlah_data_1 = data.count(1)

print(f"===JUMLAH DATA COUNT===")
print(f"jumlah data 2 = {jumlah_data_2}")
print(f"jumlah data 4 = {jumlah_data_4}")
print(f"jumlah data 1 = {jumlah_data_1}")

# cara mecari tahu posisi index
dataNama = ["ahmad", "soe", "ardi"]
print(f"ini adalah list nama : \n {dataNama}")

index_ahmad = dataNama.index("ahmad")
index_soe = dataNama.index("soe")
index_ardi = dataNama.index("ardi")

print(f"===POSISI-POSISI INDEX===")
print(f"ahmad berada dalam index : {index_ahmad}")
print(f"soe berada dalam index = {index_soe}")
print(f"ardi berada dalam index = {index_ardi}")


# mengurutkan list 
dataNama = ["ahmad", "soe", "ardi"]
print(f"angka sebelum di urutkan : \n {dataNama}")

dataNama.sort()
print(f"data setelah di urutkan : {dataNama}")

# cara membalik listnya 
dataNama.reverse()
print(f"data yang di balik : {dataNama}")