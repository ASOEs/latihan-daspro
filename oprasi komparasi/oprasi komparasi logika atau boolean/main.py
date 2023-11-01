# oprasi logika atau boolean
# not , or, and, xor

print("=====NOT=====")
# suatu oprasi yang memberi tahu bahwa suatu variabel tidak sama dengan variabel lain
# contoh :
a = True
c = not a
print("data boolean =", a)
print("---------------------NOT")
print("data boolean =", c)


print("=====OR=====")
# suatu oprasi dimana salah satu varibel memenuhi syarat tersebut dengan 
# di indentasi dengan fungsi 'OR'
# Contoh :
a = True
b = False
c = a or b
print("---------------------OR")
print(f" {a} 'OR' {b} = {c}")

a = False
b =  False
c = a or b
print(f" {a} 'OR' {b} = {c}")

a = False
b = True
c = a or b
print(f" {a} 'OR' {b} = {c}")

a = True
b = False
c = a or b
print(f" {a} 'OR' {b} = {c}")

a = True
b = True
c = a or b
print(f" {a} 'OR' {b} = {c}")

print("=====AND=====")
# and adalah satu kondisi dimana kedua varibael haru memenuhi syarat
# agar hasilnya True, dan jika salah satu variabel tidak memenuhi syarat
# maka akan menghasilkan False
# contoh
a = False
b =  False
c = a and b
print(f" {a} 'and' {b} = {c}")

a = False
b = True
c = a and b
print(f" {a} 'and' {b} = {c}")

a = True
b = False
c = a and b
print(f" {a} 'and' {b} = {c}")

a = True
b = True
c = a and b
print(f" {a} 'and' {b} = {c}")

print("=====XOR=====")
# xor akan true apabila salah satu true, dan sisanya akan false
a = False
b =  False
c = a ^ b
print(f" {a} 'XOR' {b} = {c}")

a = False
b = True
c = a ^ b
print(f" {a} 'XOR' {b} = {c}")

a = True
b = False
c = a ^ b
print(f" {a} 'XOR' {b} = {c}")

a = True
b = True
c = a ^ b
print(f" {a} 'XOR' {b} = {c}")