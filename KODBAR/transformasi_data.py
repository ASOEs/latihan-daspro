# uang = [5000, 12000, 7500, 20000, 14000]
# i = 0

# while i < len(uang):
#     uang[i] = 'Rp' + str(uang[i])
#     i += 1
# print(f"harga dalam format mata uang : {uang}")

a = int(input("angka : "))
while True:
    if a % 2 == 1 or a <= 50:
        a = int(input("masukan angka kembali : "))
    else:
        print("benarr")
        break
