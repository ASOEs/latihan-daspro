import numpy as np

'''data nilai terbesar'''
data_nilai = np.random.randint(1,20,10)
def nilai_ujian():
    nilai_ujian = np.sort(data_nilai)[::-1]
    print(f"ini adalah urutan dari yang terbesar : {nilai_ujian}")
    print(f"dan ini adalah Lima angka terbesarnya : {nilai_ujian[:2]}")

nilai_ujian()

'''celcius ke fahrenheit'''
data_celcius = np.array([28, 30, 29, 31, 27, 28, 30, 32, 31, 29])
def fahrenheit(celcius):
    hasil = (celcius * 9/5) + 32
    return hasil

print(fahrenheit(data_celcius))
