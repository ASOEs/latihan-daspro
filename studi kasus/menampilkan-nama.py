# my_dict = {
#     'nama' : 'achmad',
#     'umur' : '18thn',
#     'asal' : 'bogor'
# }

dict_baru = {

}

masukan_key = input("masukan key : ") 
masukan_value = input("masukan value : ")

dict_baru.update({masukan_key : masukan_value})
print(dict_baru)

for i, v in dict_baru.items() :
    print(i , ":", v)

# while True :
#     masukan = input("apa yang anda cari? : ")
#     if masukan == "nama":
#         print(my_dict['nama'])
#         break
#     elif masukan == "umur" :
#         print(my_dict['umur'])
#         break
#     elif masukan == "asal" :
#         print(my_dict['asal'])
#         break
#     else:
#         print("ulangi masukan kembali apa yang anda cari")
