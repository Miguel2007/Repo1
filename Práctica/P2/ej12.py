n1 = float(input("Introduzca el primer número: "))
n2 = float(input("Introduzca el segundo número: "))

op = input("Introduzca la operación a realizar: ")

if op == '+':
    print("El resultado de la suma es", n1 + n2, ".")

elif op == '-':
    print("El resultado de la resta es", n1 - n2, ".")

elif op == '/':
    if n2 == 0:
        print("No se puede dividir entre 0.")
    print("El resultado de la resta es", n1 / n2, ".")

elif op == '*':
    print("El resultado de la resta es", n1 * n2, ".")