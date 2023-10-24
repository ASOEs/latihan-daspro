dict_inputan = {

}

masukan_key = input("masukan kunci : ")
masukan_value = input("masukan nilai : ")

dict_inputan.update({masukan_key : masukan_value})

for i, v in dict_inputan.items() :
    print(i, ":", v)
