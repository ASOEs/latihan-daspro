peforma = input("masukan peforma karyawan : ")
gaji = int(input("masukan gaji anda : "))

if peforma == "sangat baik" :
    presetase_bonus = 0.2

elif peforma == "cukup" :
    presetase_bonus = 0.1

else :
    presetase_bonus = 0.05


# menghitung gaji 
total = gaji * presetase_bonus

print(f"jumlah bonus yang di terima adalah : {total}")