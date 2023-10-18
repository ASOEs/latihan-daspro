data = {
    "nama" : "none",
    "kelas" : "none",
    "umur" : "none",
    "ttl" : "none",
}


nama = data.get("nama")
kelas = data.get("kelas")
umur = data.get("umur")
ttl = data.get("ttl")

print(f"""
    nama : {nama}
    kelas : {kelas}
    umur : {umur}
    ttl : {ttl}

""")

nama = data["nama"] = input("tuliskan nama anda :")
# kelas = data["kelas"] = input("tuliskan nama anda :")
# umur = data["umur"] = input("tuliskan nama anda :")
# ttl = data["ttl"] = input("tuliskan nama anda :")


