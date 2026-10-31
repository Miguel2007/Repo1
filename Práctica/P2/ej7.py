dividendo = float(input("Introduzca el dividendo de la división: "))
divisor = float(input("Introduzca el divisor de la división: "))

if divisor == 0:
    print("Error: no se puede dividir entre 0.")

division = dividendo / divisor

print("El resultado de la división es:", division, ".")