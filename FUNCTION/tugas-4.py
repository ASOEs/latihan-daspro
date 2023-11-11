def login():
    username_sistem = "Daspro2023"
    password_sistem = "Latihan"
    kesempatan = 3

    while kesempatan > 0:
        m_username = input("masukan username anda : ")
        m_pasword = input("masukan password anda : ")

        if m_username == username_sistem and m_pasword == password_sistem:
            print("login berhasil")
            break
        else:
            kesempatan -= 1
            print(f"Log in gagal, kesempatan tersisa {kesempatan}")

        if kesempatan == 0:
            print("Anda telah mencapai batas kesempatan login. Keluar dari program.")


login()