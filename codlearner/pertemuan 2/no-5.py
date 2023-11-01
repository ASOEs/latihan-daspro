

list_nama = input("nama teman : ").lower().replace(" ", "").split(",")
dict_teman = {}

for nama in list_nama :
    if nama in dict_teman:
        dict_teman[nama] += 1
    else :
        dict_teman[nama] =1

print(dict_teman)