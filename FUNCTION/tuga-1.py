def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)

    return fib_sequence[:n]

n = int(input("Masukkan panjang deret Fibonacci: "))
hasil_fibonacci = fibonacci(n)
print(f'Deret Fibonacci dengan panjang {n}: {hasil_fibonacci}')
