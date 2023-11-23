# belajar menggunakan lambda
'''contoh function biasa'''
def f_kuadrat(angka):
    hasil = angka ** 2
    return hasil
print(f"ini adalah hasil dari kuadrat : {f_kuadrat(3)}")


'''contoh dari lambda'''
# nama function = lambda argumen: expression
kuadrat = lambda angka: angka ** 2
print(f"ini adalah kuadrat memakai fungsi lamda : {kuadrat(4)}")

# conoth lambda dengan dua input atau dua argumen
pangkat = lambda pangkat, pow : pangkat ** pow
print(f"ini adalah lambda dengan dua input atau argumen = {pangkat(6,2)}")

'''kegunaan lambda'''
# sorting list biasa 
data_list = ["ahmad", "ardi", "soe"]
data_list.sort()
print(f"sorted list biasa : \n {data_list}")
data_list.sort(key=len) #memakai key
print(f"sorted list by len : \n {data_list}")

def panjang_nama(nama): #memakai function
    return len(nama)
data_list.sort(key=panjang_nama)
print(f"sorted list menggunakan function : {data_list}")

# sorted list by lambda 
data_list = ["ahmad", "ardi", "soe"]
data_list.sort(key=lambda nama : len(nama))
print(f"sorted list by lambda : {data_list}")

'''filtered data'''
print("="*90)
list_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
# memakai function
def angka_genap(angka):
    return angka %2 == 0
data_angka_baru = list(filter(angka_genap,list_angka))
print(f"data angka genap : {data_angka_baru}")

# memakai lambda 
data_angka_baru  = list(filter(lambda x : x %2 == 0, list_angka))
print(f"data angka genap with lambda : {data_angka_baru}")

data_angka_ganjil = list(filter(lambda x : x %2 == 1, list_angka))
print(f"data angka ganjil with lambda : {data_angka_ganjil}")

kelipatan_tiga = list(filter(lambda y : (y %3 == 0), list_angka))
print(f"kelipatan 3 : {kelipatan_tiga}")