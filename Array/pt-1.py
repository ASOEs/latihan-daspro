import numpy as np

'''pengenalan array'''
print("="*20)
array = np.array([1,2,3,4,5])
print(array)
print(type(array))
print("="*20)
# data_list = [1,2,3,4,5]
# print(data_list)
# print(type(data_list))

'''cara mengakses array'''
print("="*20)
arr = np.array([1,2,3,4,5])
print(arr)
print(arr[1]) #untuk mengakses index 1
print(arr[2:5]) #untuk mengakses index 2 sampai 5
print(arr[0] + arr[4]) #menjumlahkan index 0 dengan 4 yaitu 1 ditambah 5 = 6
print("="*20)


'''dimensi pada array'''
# satu dimensi
print("="*20)
arr_1 = np.array([1,2,3,4])
print(f"ini adalah dimensi : {arr_1.ndim}") #untuk mengetahui ini dimensi berapa
print(arr_1)

# dua dimensi
print("="*20)
arr_2 = np.array([[1,2],[3,4]])
print(f"ini adalah dimensi : {arr_2.ndim}")
print(arr_2)

# tiga dimensi
print("="*20)
arr_3 = np.array([[[1,2],[3,4],[5,6],[7,8],[9,10]]])
print(f"ini adalah dimensi : {arr_3.ndim}")
print(arr_3)

