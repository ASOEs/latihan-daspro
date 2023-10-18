# casting meruopakan cara mengubah satu tipe ke ke tipe lainnya
# contohnya integer ke boolean atau integer ke float
#  tipe data : int, str, float, bool


##INTEGER
print("====INTEGER====")

data_int = 9
data_float = float(data_int)
data_bool = bool(data_int)
data_str = str(data_int)
print("data :", data_int, type(data_int))
print("data :", data_float, type(data_float))
print("data :", data_bool, type(data_bool)) #jika nilai bool = 0 maka hasilnya akan false
print("data :", data_str, type(data_str))

##FLOAT
print("====FLOAT====")

data_float = 9.5
data_int = int(data_float)
data_bool = bool(data_float)
data_str = str(data_float)
print("data :", data_float, type(data_float))
print("data :", data_int, type(data_int)) #akan di blatkan ke bawah
print("data :", data_bool, type(data_bool)) #jika nilai bool = 0 maka hasilnya akan false
print("data :", data_str, type(data_str))


##BOOLEAN
print("====BOOLEAN====")

data_bool = False
data_int = int(data_bool)
data_bool = bool(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data :", data_int, type(data_int)) #akan di blatkan ke bawah
print("data :", data_bool, type(data_bool)) #jika nilai bool = 0 maka hasilnya akan false
print("data :", data_str, type(data_str))
print("data :", data_float, type(data_float))

##STRING
print("===STRING===")
data_string = "10";
data_int = int(data_string)
data_float= float(data_string)
data_bool = bool(data_string)
print("data :", data_string, type(data_str))
print("data :", data_int, type(data_int)) #string harus angka
print("data :", data_float, type(data_float)) #string harus angkaSS
print("data :", data_bool, type(data_bool)) #false jika string kosong







