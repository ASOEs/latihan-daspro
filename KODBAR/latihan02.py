kelipatan_4 = 0
kelipatan_5 = 0
empat = 0
lima = 0

i = 0
while i >= 0:
    i = int(input("masukan angka : "))
    if i % 4 == 0:
        empat += i
    if i % 5 == 0:
        lima += i

print(f"jumlah bilangan kelipatan 4 : {empat}")
print(f"jumlah bilangan kelipatan 5 : {lima}")
