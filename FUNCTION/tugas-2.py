def hitungVolume(radius, tinggi):
    volume = 3.14 * radius**2 * tinggi
    return volume

radius = float(input("masukan angka : "))
tinggi = float(input("masukan tinggi : "))

volume_tabung = hitungVolume(radius,tinggi)

print(f"volume dari tabung itu adalah : ")