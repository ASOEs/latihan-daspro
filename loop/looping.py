# for i in range(1, 51) :  #range hanya bisa di gunakan untuk numeric atau integer
#     if i % 5 == 0:
#         print("pass")
#     else:
#         print(i)

# for i in range(1,6) :
#     print(i)



# buah = ["apel", "belimbing", "ceri", "durian"]
# for i in buah:
#     print(f"buah : {i}")


# # jika memakai list range
# for i in range(len(buah)) :
#     print(f"Buah : {buah[i]}")

# while akan terus berjalan jika kondisi bernilai true
# contoh
# angka = 0
# while(angka < 8) :
#     print(f"angka sekarang : {angka}")
#     angka += 1

# control the flow ada break dan ada continue
# contoh
# angka = [1,2,3,4,5] #break
# for i in angka :
#     print(i)
#     if i == 3 :
#         break

# for i in range(0, 105, 5): (0=dari 0, 105=sampai 105, 5=kelipatan 5)
#     print(i)

# for i in range(0,100,5):
#     print(i)
#     print("RPL")
# print("hello world")

# nested loooping
# buah = ["apel", "belimbing", "ceri"]
# angka = [1,2]

# for i in buah:
#     for j in angka :
#         print(i)
#         print(j)

while True :
    bilangan = int(input("masukan nilai ganjil > 50 : "))
    if bilangan % 2 == 1 and bilangan > 50:
        print("benar")
        break
    else :
        print("salah inputkan lagi")



