far = float(input("Introduzca la temperatura en grados Fahrenheit: "))
print("El equivalente en grados celsius de", far, "F son:", (far - 32) / 1.8, "C")

if (far - 32) / 1.8 > 0:
    print("Temperatura mayor a 0 grados Celsius.")