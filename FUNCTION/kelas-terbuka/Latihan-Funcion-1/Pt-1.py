'''fungsi dengan argument'''
'''
def nama_fungsi():
    Badan fungsi
'''

def hello_world(nama):
    '''fungsi hellow world menerima input dengan nama'''
    print(f"selamat datang dunia wahai {nama}")

nama = input("masukan nama anda : ")
hello_world(nama)



# program tambah 
def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(10,5)

# program say hi
def absen(list_nama):
    data_peserta = list_nama.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

list_absen = ["ahmad","soe","ardi"]
absen(list_absen)