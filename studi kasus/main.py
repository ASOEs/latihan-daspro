my_dict = {
    'nama' : 'ahmad',
    'umur' : '8 tahun'
}

print(my_dict)

# key = input("masukan key : ")
value = input("masukan nama anda : ")
value2 = input("masukan umur anda : ")

my_dict.update({'nama': value})
my_dict.update({'umur': value2})

print(my_dict)

for i,v in my_dict.items():
    print(i,v)