# perulangan (loop)
# for kondisi
# aksi

# ini dengan list
angka = [1,2,3,4,5]
print(angka)

for i in angka:
    print(f"i sekarang --> {i}")

print("akkhir dari program 1")

# ini dengan range
angka_2 = range(5)

for i in range(5):
    print(f"i sekarang --> {i}")

print("akkhir dari program 2")


angka_2 = range(1,5)

for i in angka_2:
    print(f"i sekarang --> {i}")

print("akkhir dari program 3")


# menggunakan str

data_str = "saya dan ucup bermain"
for huruf in data_str:
    print(huruf)