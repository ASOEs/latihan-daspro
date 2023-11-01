kalimat = input("masukan kalimat anda : ").split()
batasHuruf = int(input("masukan batas hurfu anda : "))

list_kata_melebihi = []
for kata in kalimat:
    if len(kata) > batasHuruf:
        list_kata_melebihi.append(kata)

print(list_kata_melebihi)
