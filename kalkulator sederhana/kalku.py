# ada 3 input
# angka_1 , angka_2 , dan oprator
# menggunakan percabangan

print(10 * "=")
print("KALKULATOR SEDERHANA")
print(10 * "=")



angka_1 = float(input("masukan angka 1 = "))
oprator = input("masukan oprator yang anda inginnkan (+,-,x,/) = ")
angka_2 = float(input("masukan angka 2 =  "))

# percabangan

if oprator == "+" :
    hasil = angka_1 + angka_2 
    print(f"ini adalah hasilnya : {hasil}")

elif oprator == "-":
    hasil = angka_1 - angka_2
    print(f"ini adalah hasilnya : {hasil}")

elif oprator == "x" :
    hasil = angka_1 * angka_2
    print(f"ini adalah hasilnya : {hasil}")

elif oprator == "/" :
    hasil = angka_1 / angka_2
    print(f"ini adalah hasilnya : {hasil}")

else :
    print("masukan opratornya")