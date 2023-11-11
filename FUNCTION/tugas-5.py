def hitung_selisih_waktu(mulai_jam, mulai_menit, mulai_detik, selesai_jam, selesai_menit, selesai_detik):
    total_detik_mulai = mulai_jam * 3600 + mulai_menit * 60 + mulai_detik
    total_detik_selesai = selesai_jam * 3600 + selesai_menit * 60 + selesai_detik

    selisih_detik = total_detik_selesai - total_detik_mulai
    jam = selisih_detik // 3600
    menit = (selisih_detik % 3600) // 60
    detik = selisih_detik % 60

    return jam, menit, detik


mulai_jam = int(input("Jam mulai: "))
mulai_menit = int(input("Menit mulai: "))
mulai_detik = int(input("Detik mulai: "))


selesai_jam = int(input("Jam selesai: "))
selesai_menit = int(input("Menit selesai: "))
selesai_detik = int(input("Detik selesai: "))

hasil_selisih = hitung_selisih_waktu(mulai_jam, mulai_menit, mulai_detik, selesai_jam, selesai_menit, selesai_detik)

print(f'Selisih waktu: {hasil_selisih[0]} jam - {hasil_selisih[1]} menit - {hasil_selisih[2]} detik')
