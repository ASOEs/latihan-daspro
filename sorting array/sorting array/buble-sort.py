# buble sort
# data_list = [1,4,2,5,7,6,9,8]
# for i in range(len(data_list)):
#     for j in range(len(data_list)-i-1):
#         if data_list[j] > data_list[j + 1]:
#             data_list[j], data_list[j+1] = data_list[j + 1], data_list[j]

# print(data_list)

# def sorting(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1], list[j]
#     return list

# heap sorting
import time 
def heapify(arr, n, i):
    largest = i  # Menginisialisasi node terbesar sebagai root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Memeriksa apakah left child dari root ada dan lebih besar dari root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Memeriksa apakah right child dari root ada dan lebih besar dari root
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Jika node terbesar bukan root, lakukan pertukaran dengan root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Membangun max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Ekstraksi elemen satu per satu dari heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Contoh penggunaan
arr = [12, 11, 13, 5, 6, 7]
print("Array sebelum diurutkan:", arr)
mulai = time.time()
heap_sort(arr)
selesai = time.time()
print("Array setelah diurutkan:", arr)
print(f"run time {selesai - mulai}")


# def heap_sorting(arr,size,index):
#     parent_index = index
#     kiri = 2 * index + 1
#     kanan = 2 * index + 2

#     # cek kiri
#     if kiri < size and arr[kiri] > arr[parent_index]:
#         parent_index = kiri
#     # cek kanan
#     if kanan < size and arr[kanan] > arr[parent_index]:
#         parent_index = kanan
    
#     if parent_index != size:
#         arr[index], arr[parent_index] = arr[index], arr[parent_index]
#         heap_sorting(arr,size,index)

# def heap_sort(arr):
#     n = len(arr)
#     # max heap
#     for i in range(n// 2-1,-1,-1):
#         heap_sorting(arr,n,index)