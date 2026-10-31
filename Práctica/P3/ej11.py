num = 0
sum_pares = 0
pares = 0
sum_impares = 0
impares = 0
num1 = []

for i in range(10):
    num = int(input("Introduzca 10 números enteros: "))
    num1.append(num)

    if num1[i] % 2 == 0:
        sum_pares += num1[i]
        pares += 1
    else:
        sum_impares += num1[i]
        impares += 1
med_impares = sum_impares / impares

print("La suma de los pares es:", sum_pares)
print("Hay", pares, "números pares.")
print("La media aritmética de los números impares es: ", med_impares)

    