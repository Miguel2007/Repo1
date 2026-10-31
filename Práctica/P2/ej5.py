cal = int(input("Introduzca una calificación entre 0 y 10: "))

while cal < 0 or cal > 10:
    cal = int(input("Error: introduzca un valor válido: "))

if cal >= 0 and cal <= 4.9:
    print("Nota insuficiente.")
elif cal >=5 and cal <= 5.9:
    print("Nota suficiente.")
elif cal >=6 and cal <= 6.9:
    print("Nota bien.")
elif cal >=7 and cal <= 8.9:
    print("Nota notable.")
elif cal >=9 and cal <= 10:
    print("Nota sobresaliente.")
