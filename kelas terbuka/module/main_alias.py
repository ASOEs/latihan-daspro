# membuat modul
from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as pk
# from matematika import * 
hasil_tambah = add(8,9)
print(f"ini adalah hasil tambah : {hasil_tambah}")

hasil_kali = k(8,9,10,2)
print(f"ini adalah hasil kali : {hasil_kali}")

hasil_pangkat = pk(3)
print(f"ini adalah hasil pangkat : {hasil_pangkat(2)}")
