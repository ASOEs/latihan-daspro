import numpy as np

# Nama : Achmad Soewadi
# NIM : 2301508
# Kelas : RPL 1-A


'''data nilai siswa'''
# saya menggunakan data random dari range 50 sampai 100  dengan 30 item
data_nilai = np.random.randint(50,100,30)
print(f"Nilai Ujian Siswa : \n {data_nilai}")

print("="*90)
# saya mengurutkan data nilai dari yang terbesar 
nilai_ujian = np.sort(data_nilai)[::-1]
print(f"Urutan Nilai dari yang terbesar : \n {nilai_ujian}")

print("="*90)
# lalu disini saya mengambil nilai yang paling 5 nilai yang paling besar
print(f"5 Nilai Terbesar : \n {nilai_ujian[:5]}")





# data_nilai = np.array([28, 30, 29, 31, 27, 28, 30, 32, 31, 29])
# sorted_arr = np.sort(data_nilai)
# print(sorted_arr)