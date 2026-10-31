edad = int(input("Introduzca su edad: "))
ing = float(input("Introduzca sus ingresos mensuales: "))

if edad > 16 and ing >= 1000:
    print("Usted debe tributar.")
else:
    print("No tiene que tributar.")