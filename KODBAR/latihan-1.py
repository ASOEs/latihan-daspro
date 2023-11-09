while True:
    nim = int(input("masukan nim anda : "))
    if nim > 0 and nim <= 300:
        if nim %2 == 0:
            print("anda masuk ke kelas A-1")
            break
        else :
            print("anda masuk ke kelas A-2")
            break
    elif nim >= 300 and nim <= 800:
        if nim %2 == 0:
            print("anda masuk ke kelas B-1")
            break
        else :
            print("anda masuk ke kelas B-2")
            break
    elif nim >= 800:
        if nim %2 == 0:
            print("anda masuk ke kelas C-1")
            break
        else:
            print("anda masuk ke kelas C-2")
            break

    else:
        print("nim anda salah")
