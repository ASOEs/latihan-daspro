total_belanja = float(input("masukan total anda belanja :"))

if total_belanja > 500000 :
    diskon = total_belanja * 0.1

    total_bayar = total_belanja - diskon

    print("pelanggan berhak mendapatkan diskon sebesar 10%")
    print(f"Total yang belanja yang harus di bayar adalah : Rp{total_bayar}")

else :
    print("pelanggan tidak mendapatkan diskon")
    print(f"total yang harus di bayar : Rp{total_belanja}")

