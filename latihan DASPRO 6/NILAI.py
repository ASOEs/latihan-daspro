nilai = float(input("masukan nilai anda : "))

if nilai >= 90 :
   grade = "A"

elif nilai >= 80 :
   grade = "B"

elif nilai >= 70 :
   grade = "C"

else :
   grade = "D"

print(f"Nilai anda adalah : {grade}")