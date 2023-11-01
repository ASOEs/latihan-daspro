# # membuat gabungan area rentang dari angka 
# # ++++3--------10+++++

# inputUser = float(input("masukan angka yang bernilai lebih dari 3 atau kurang dari 10 : "))

# # ++++++3-------
# # memeriksa angka kurang dari 
# iskurangDari = (inputUser < 3)
# print(f"kurang dari 3 = {iskurangDari}")

# # -----10++++
# # memeriksa lebih dari
# islebihDari = (inputUser > 10)
# print(f"Lebih dari 10 = {islebihDari}")

# # +++3----10+++
# # gabungan
# isCorrect = iskurangDari or islebihDari
# print(f"angkka yang anda masukan {isCorrect}")


# # ----3+++10---
# # kasus irisan
# inputUser = float(input("masukan angka yang bernilai lebih dari 3 dan kurang dari 10 : "))
# # ----3+++++
# # memeriksa lebih dari 3
# islebihDari = inputUser > 3
# print(f"lebih dari 3 = {islebihDari}")

# # ++++10----
# iskurangDari = inputUser < 10
# print(f"kurang dari 10 = {iskurangDari}")


# isCorrect = iskurangDari and islebihDari
# print(f"angka yang anda masukan = {isCorrect}")


# pr
# 1. ----0++++5-----8+++++11-----
inputUser = float(input("masukan angka lebih dari 0 \n kurang dari 5 \n lebih dari 8 \n kurang dari 11 \n = "))
    # memeriksa kurang dari 0
islebihDari0 = inputUser > 0
print(f"lebih dari 0 = {islebihDari0}")

    # memeriksa kurang dari 5
isKurangDari5 = inputUser < 5
print(f"kurang dari 5 = {isKurangDari5}")

    # memeriksa lebih dari 8
islebihdari8 = inputUser > 8
print(f"lebih dari 8 = {islebihdari8}")

    # memeriksa kurang dari 11
isKurangDari11 = inputUser < 11
print(f"kurang dari 11 = {isKurangDari11}")

# irisan
isCorrect = islebihDari0 or isKurangDari5 , islebihdari8 or isKurangDari11
print(f"angka yang anda masukan = {isCorrect}")
# 2. ++++0----5+++++8-----11+++++

