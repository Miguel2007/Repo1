edad = int(input("Introduzca su edad: "))


while edad > 120:
    edad = int(input("Introduzca un valor correcto: "))
    for i in range(1, edad + 1):
        print(i)
