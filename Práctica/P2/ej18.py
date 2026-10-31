edad = int(input("Introduzca la edad del cliente: "))

if edad < 4:
    print("Entrada gratuita.")
elif edad >= 4 and edad < 18:
    print("El precio es de 5€.")
elif edad >= 18:
    print("El precio es de 10€.")