ent = int(input("Introduzca un número entero positivo: "))

while ent < 0:
    ent = int(input("Introduzca un número válido: "))
    for i in range(1,ent + 1,2):
        print (i, end = ",")    
