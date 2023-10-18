a = {"anjing", "kucing", "ikan", "rusa"}
print(f"ini adalah set : {a}")
print(len(a))

# cara menghapus
a.pop()
print(a)

# cara menambah
a.add("ahmad")
print(a)

# cara menambha dengan set lain
b = {"ahmad", "asu", "ucup"}
c = a.union(b)
print(c)

# cara memanggil set
for item in a :
    print(item)
