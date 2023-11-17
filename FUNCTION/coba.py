
'''login'''
# def daftar():
#     data_meja = [1,2,3,4,5,6,7,8,9,10]


#     while True:
#         no_meja = int(input("nomor meja yang anda tempati : "))
#         if no_meja == len(data_meja):
#             print("mejanya ada!")
#             break
#         else :
#             print(f"mejanya ga ada! kesempatan anda adalah")

# daftar()


'''menghitung rata rata dan total dari list'''
# def hitung_total(*args):
#     total = sum(args)
#     rata_rata = total / len(args)
#     return total, rata_rata

# angka = input("masukan nilai anda : ")
# data_nilai = [int(nilai) for nilai in angka.split(",")]

# rata_rata, total = hitung_total(*data_nilai)
# print(f"total = {total}")
# print(f"rata rata : {rata_rata}")

'''faktorial'''
# def faktorial(nilai):
#     for i in range(0,nilai):
#         if i + 1 == nilai:
#             print(f"{nilai - i}! = {nilai - i}")
#         else :
#             print(f"{nilai - i}! = {nilai - i}*{nilai - i - 1} ")

# faktorial(int(input("masukan nilai anda : ")))

'''bilangan bulat dan kelipatan 4 dan 5'''
# def kelipatan():
#     habis_dibagi_4 = []
#     habis_dibagi_5 = []
#     while True:
#         angka = int(input("masukan angka anda : "))
#         if angka < 0:
#             break
#         elif angka >= 0:
#             if angka % 4 == 0:
#                 habis_dibagi_4.append(angka)
#             elif angka % 5 == 0:
#                 habis_dibagi_5.append(angka)
#             else:
#                 continue
#     print(f'{sum(habis_dibagi_4)}')
#     print(f'{sum(habis_dibagi_5)}')
    
# kelipatan()


''''''
