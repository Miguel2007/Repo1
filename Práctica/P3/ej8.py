
num1 = 0
num2 = 0
condicion = ""
while condicion.upper() != 'N':
    num1 = float(input("Introduzca el primer número: "))
    num2 = float(input("Introduzca el segundo número: "))
    print("La suma es:", num1 + num2)
    condicion = input("¿Desea continuar?(Y/N): ")

