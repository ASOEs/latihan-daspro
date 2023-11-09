faktorial = int(input("faltorial : "))
for i in range(0, faktorial):
    if i + 1 == faktorial:
        print(f"{faktorial-i}! = {faktorial-i}")
    else:
        print(f"{faktorial-i}! = {faktorial-i}*{faktorial-i-1}")
