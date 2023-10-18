<<<<<<< HEAD
# operator dictionary

data_dict = {
    'cp' : 'ucup',
    'otong' : 'otong',
    'dg' : 'dudung'
}

# mengambil panjang dari dictionary
lendict = len(data_dict)
print(lendict)

# mengecek key exist(ada) atau tidak
key = 'cp'
chekkey = key in data_dict
print(f"apakah {key} ada pada data_dict : {chekkey}") #cek data dengan masage

# mengakses value (read) dengan get
print(data_dict.get('cp'))
print(data_dict.get('kis',"data tidak di temuka"))

# cara update data
data_dict.update({"cp" : "ucup"})
print(data_dict)

data_dict.update({'ahmad' : 'kerenn '}) #bisa menambah value baru jika value tersebut tidak ada di dictionary
print(data_dict)

# cara mneghapus data pada dict
del data_dict["ahmad"]
=======
# operator dictionary

data_dict = {
    'cp' : 'ucup',
    'otong' : 'otong',
    'dg' : 'dudung'
}

# mengambil panjang dari dictionary
lendict = len(data_dict)
print(lendict)

# mengecek key exist(ada) atau tidak
key = 'cp'
chekkey = key in data_dict
print(f"apakah {key} ada pada data_dict : {chekkey}") #cek data dengan masage

# mengakses value (read) dengan get
print(data_dict.get('cp'))
print(data_dict.get('kis',"data tidak di temuka"))

# cara update data
data_dict.update({"cp" : "ucup"})
print(data_dict)

data_dict.update({'ahmad' : 'kerenn '}) #bisa menambah value baru jika value tersebut tidak ada di dictionary
print(data_dict)

# cara mneghapus data pada dict
del data_dict["ahmad"]
>>>>>>> 481d72619d31d25a3ba0160176609a715e3b1311
print(data_dict)