import numpy as np 

# membuat array menggunakan np
# array = np.array([1,2,3,4,5])
# print(array)

def C_to_F(celciius):
    return 9/5 * celciius + 32

def random_arr(low,high,size):
    data_celcius = np.random.default_rng()
    return data_celcius.integers(low=low,high=high,size=size)


suhu_singapura = random_arr(0,100,10)
print(f"celcius suhu singapura : {suhu_singapura}")

suhu_fahrenheit = C_to_F(suhu_singapura)
print(f"suhu yang telah di convert : {suhu_fahrenheit}")

