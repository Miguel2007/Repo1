def fibonacci_hasta(numero):
   
    fib = [0, 1]
    i = 1
    sum = 0
    while sum < numero:
        sum = fib[i] + fib[i-1]
        if sum <= numero:
            fib.append(sum)
        i += 1
    return fib

num = float(input("Introduzca un número: "))
f = fibonacci_hasta(num)
print(f)