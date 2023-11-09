data = [5, 12, 8, 20, 7, 14, 11]
f_data = []

i = 0
while i < len(data):
    if data[i] > 10:
        f_data.append(data[i])
    i += 1

    print(f"data yang sudah di filter = {f_data}")
