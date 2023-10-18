# conoth penggunaan nested list
# misalkan kita mempunyai beberapa list peserta yang berisikan nama,umur,dan gender
peserta0 = ["ucup",23,"laki"]
peserta1 = ["duduh",24,"laki"]
peserta2 = ["alek",21,"cewek"]

# gabungkan list diatas
list_peserta = [peserta0, peserta1, peserta2]
print(f"ini adalah daftar peserta : {list_peserta}")

# agar tampilannya lebih menarik kita gunakan loop
for peserta in list_peserta :
    print(f"nama \t : {peserta[0]}")
    print(f"umur \t : {peserta[1]}")
    print(f"umur \t : {peserta[2]} \n")