num = int(input("Introduzca un número entero positivo: "))
sum = 0
while num != 0:
    dig = num % 10
    sum += dig
    num = num // 10
print("La suma de sus dígitos es:", sum)
