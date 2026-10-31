def es_par(n):
    if n % 2 == 0:
        print(n, "es par.")
    elif n % 2 != 0:
        print(n, "es impar.")

num = float(input("Introduzca un número: "))

es_par(num)