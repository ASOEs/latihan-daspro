'''args'''

# memasukan data/argument ke dalam fungsi
# def fungsi(nama,tinggi,berat):
#     print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

# fungsi("ucup",170,40)

# perkenalkan nama saya args dengan ciri memkai *
# def fungsi(*args):
#     nama = args[0]
#     tinggi = args[1]
#     berat = args[2]
#     print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

# fungsi("dudung",100,50)

# studi kasus 
def tambah(*data):
    # data tipenya adalah tuple dan bisa di iterasi
    output = 0
    for i in data:
        output += i
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil : {hasil}")