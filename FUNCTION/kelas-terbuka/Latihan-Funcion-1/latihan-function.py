'''latihan fungsi'''

import os

# program menghitung luast dan keliling persegi panjang


# membuat header program

# os.system("cls")
# print(f"{'PRGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # mengambil inputa user
# panjang = int(input("masukan nilai panjang : "))
# lebar = int(input("masukan nilai lebar  : "))

# # menghitung nilai luas dan keliling
# luas = panjang * lebar
# keliling = 2*(panjang + lebar)

# # tampilam hasil
# print(f"hasil perhitungan luas adalah : {luas}")
# print(f"hasil perhitungan keliling adalah : {keliling}")

def header():
    '''header'''
    os.system("cls")
    print(f"{'PRGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    panjang = int(input("masukan nilai panjang : "))
    lebar = int(input("masukan nilai lebar  : "))
    return panjang, lebar

def hitungLuas(lebar,panjang):
    '''hitung luas'''
    return  panjang * lebar

def hitungKeliling(lebar,panjang):
    return 2 * (panjang + lebar)

def display(massage,value):
    print(f"hasil perhitungan {massage} : {value}")
# proram utama 
while True:
    header()
    lebar, panjang = input_user()
    luas = hitungLuas(lebar, panjang)
    keliling = hitungKeliling(lebar,panjang)

    display("luas", luas)
    display("keliling", keliling)

    IsContinue = input("apakah lanjut (y/n)? ")
    if IsContinue == "n":
        print(f"Program selesai terimakasih..")
        break
