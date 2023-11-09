data =  [5, 12, 8, 20, 7, 14, 11]
filter_data = []
i = 0

while i < len(data):
    if data[i] > 10:
        filter_data.append(data)
    i += 1


print(f"data yang sudah di liter {filter_data}")