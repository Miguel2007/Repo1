vacio = {}
edad = int(input("Introduzca su edad: "))
sexo = input("Introduzca su sexo: ")
tele = int(input("Introduzca su número de teléfono: "))
email = input("Introduzca su correo electrónico: ")

vacio.update({"Edad": edad, "Sexo": sexo, "Teléfono": tele, "Correo electrónico": email})


print("Datos de la persona:")
for i, para in vacio.items():
    print(i, para)