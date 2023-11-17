'''default argument'''

# template
# def fungsi(argument = value):
#     badan argument

# contoh 1
def say_hello(nama = "kamu"):
    print(f"hallo {nama}")

say_hello()

# contoh 2
def sapa(nama , pesan = "apa kabar?"):
    print(f"haii {nama} {pesan}")

sapa("ahmad")

# contoh 2
def hitung_pangkat(angka, pangkat = 2):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(3))

# contoh 4
def pangkat(input1 = 1, input2= 2, input3 = 3, input4 = 4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(pangkat())
print(pangkat(input1=4,input2=4))