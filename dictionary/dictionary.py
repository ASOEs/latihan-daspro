# list -> aray, mengakses data dengan menggunakan index
# contoh
# data_list = [1,2,3,4,5]
# print(data_list[0])

# dictionary (dict)  --> associative array
# identifier --> key untuk mengakses data 
data_dict = {
    'key': 'value',
    'cp' : 'ucupp',
    'tg' : 'otong',
    'dg' : 'dudung'
}

# print(f"ini adalah bentuk dictionary : \n {data_dict}")

# # cara memanggil item pada dictionari adalah :
# print(data_dict['cp'])

# # mangakses item dict dengan get
# print(data_dict.get('cp'))

cp = data_dict.get('cp')
print(cp)