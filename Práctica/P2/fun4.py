def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area
bas = float(input("Introduzca la base del triángulo: "))
alt = float(input("Introduzca la altura del triángulo: "))

superficie = area_triangulo(bas,alt)

print("El área del triángulo es de", superficie)
