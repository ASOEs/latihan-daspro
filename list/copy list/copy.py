## teknik menduplikat list
# misalkan kita mempunyai sebah list 
a = ["ahmad", "soe", "ardi"]
print(f"a = {a}")

# lalu kita ingin mnecopy list a dengan list yang baru yaiutu list b
b = a
print(f"b = {b}")

# lalu kita akan mencoba merubah member dari list a 
a[0] = "soewardi"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# hasilnya akan berubah yang b juga apabila list a ada yang berubah dikarenakan :
# address dari kedua list itu sama 
# bagaimna cara membuktikanya? yaitu dengan cara :
print(f" addres a = {hex(id(a))}")
print(f" addres b = {hex(id(b))}")

# cara menduplikat yang benar adalah :
print(f"=====COPY LIST=====")
c = a.copy()
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

c[0] = "ahmad"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")