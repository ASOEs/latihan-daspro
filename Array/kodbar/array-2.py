import numpy as np

def random_arr(low,high,size):
    data_nilai = np.random.default_rng()
    return data_nilai.integers(low=low, high=high,size=size)

nilai = random_arr(20,100,30)
sort = np.sort(nilai)[::-1]
print(sort)
nilai_ujian = sort[:5]
print(nilai_ujian)