# function and prosedure
# function dan prosedur adalah bagian kecil yang
# berada dalam program utama yang di gunakam untuk
# menyelesaikan masalah khusus dengan parameter yang
# diberikan 

# FUNCTION
# merupakan proses diantara sebuat input dan output
# fungsi menggunakan pernyataan "return" untuk mengembalikan nilai

# PROSEDUR
# prosedur sama sama menerima input tapi tidak mengembalikan nilai
# prosedur di gunakan untuk mengeksekusi tindakan tertentu tanpa prelu mengembalikan nilai
# contoh

# contoh function
def penjumlahan(a,b):
    hasil = a + b 
    return hasil

print(penjumlahan(2,3))

# contoh prosedur
def greeting(nama):
    print(f"halo, {nama}")

greeting("ahmad")

# contoh globar var
globalVar = 10
def flobalFunction():
    print(f"nilai dari global variabel adalah {globalVar}")

flobalFunction()

# local var
def localFunction():
    localVar = 5
    print(f"Nilai dari local Variabel adalah {localVar}")

localFunction()


def perkenalan(nama):
    print(f"halo, {nama}")

greeting(input("masukan nama anda : "))