'''type hint untuk fungsi'''

def fungsi_sepuluh(args:int) -> int :
    output = 10 ** args
    return output

hasil = fungsi_sepuluh(2)
print(hasil)

def display(args : str) -> str :
    print(args)

display("ahmad")