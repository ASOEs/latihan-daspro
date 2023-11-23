'''belajar **kwargs'''

# studi kasus
def math(*args,**kwargs):
    otuput = 0
    if kwargs["option"] == "tambah":
        for i in args:
            otuput += i
    elif kwargs["option"] == "kali":
        otuput = 1
        for i in args:
            otuput *= i
    return otuput

hasil = math(1,2,3,4, option = "tambah")
print(hasil)

hasil = math(1,2,3,4, option = "kali")
print(hasil)