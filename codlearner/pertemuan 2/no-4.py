list_awal = input("masukan list awal : ").split(",")
list_filter = input("masukan filter : ").split(",")
print(list_awal)

list_hasil = list_awal.copy()

for item_awal in list_awal :
    for item_filter in list_filter:
        if item_awal == item_filter :
            list_hasil.remove(item_filter)

print(list_hasil)