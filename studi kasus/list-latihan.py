buah = ["apel", "jeruk", "mangga", "durian", "strawberry", "dukuh"]
print("="*5, "List Latihan", "="*5)
for i in buah:
    print(i)

print("="*5, "mengambil list ke 2-5", "="*5)
print(buah[2 : 5])

print("="*5, "menghapus item bernama apel", "="*5)
print(f"ini adalah list yang belum di update : \n {buah}")
buah.pop(0)
print(f"ini adalah list yang sudah di update : \n {buah}")


print("="*5, "mengganti nama jeruk jadi anggru", "="*5)
buah[0] = "anggur"
print(buah)

# menambakan leci di indx ke 3
buah.insert(3,"leci")
print(buah)

# mengurutkan list
buah.sort()
print(buah)