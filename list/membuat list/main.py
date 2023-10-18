# ====list====

# kumpulan data number
data_angka = [1,2,3,4,5]
print(data_angka)

# kumoulan data string
data_str = ["ahmad","soe","ardi"]
print(data_str)

# kumpulan data boolean
data_bool = [True,False]
print(data_bool)

# bisa juga di campur antara number,str,bool

# membuat list dengan for loop, list comprehensian
data_list_pake_for = [i**2 for i in range(0,10)]
print(data_list_pake_for) 

# membuat list pake for if
list_pake_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_pake_for_if)

list_pake_for_if2 = [ i for i in range(0,10) if i %2 !=0]
print(list_pake_for_if2)