punt = float(input("Introduzca su puntuación: "))

if punt >= 0 and punt <= 0.3:
    print("Nivel de rendimiento inaceptable.")
    print("Su bonificación es de", punt*2400, "€.")
if punt >= 0.4 and punt <= 0.5:
    print("Nivel de rendimiento aceptable.")
    print("Su bonificación es de", punt*2400, "€.")
if punt >= 0.6 and punt <= 1:
    print("Nivel de rendimiento meritorio.")
    print("Su bonificación es de", punt*2400, "€.")
else:
    print("Error: puntuación invalida.")