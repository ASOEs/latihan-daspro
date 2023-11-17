'''fungsi dengan pengembalian return'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#     badan nama_fungsi
#     return output

# fungsi kudrat
# def fungsi_kuadrat(input_angka):
#     output = input_angka**2
#     return output

# y = fungsi_kuadrat(5)
# print(y)

# fungsi oprasi aritmatika
def oprasi_aritmatika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah, kurang, kali, bagi

k,l,m,n = oprasi_aritmatika(9,5)
print(f"hasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil kali = {m}")
print(f"hasil  bagi = {n}")