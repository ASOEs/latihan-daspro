# Nama : Achmad Soewardi
# NIM : 2301508
# Kelas : RPL-1A


import numpy as np

arr_celcius = np.array([28, 30, 29, 31, 27, 28, 30, 32, 31, 29])

suhu_fahrenheit = (arr_celcius * 9/5) + 32

print(f"ini adalah suhu dalam celcius :  \n {arr_celcius}")
print(f"ini adalah suhu dalam fahenheit : \n {suhu_fahrenheit}")

