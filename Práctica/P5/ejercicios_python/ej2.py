def datos(dni, nombre, notas):

    estudiante = {}
    estudiante.update({"DNI": dni, "Nombre": nombre, "Notas": notas})
    
    return estudiante

num = int(input("Introduzca el número de registros que desea crear: "))

lista_estudiantes = []

for i in range(1,num + 1):
    print(f"Introduce los datos del alumno {i}:\n" )

    dni = input("DNI: ")
    nombre = input("Nombre: ")
    fin = False
    notas = []

    while fin == False:

        nota = int(input("Notas(-1 para terminar): "))
        if nota != -1:
            notas.append(nota)
        elif nota == -1:
            fin = True
            print(datos(dni, nombre, notas))

    lista_estudiantes.append(datos(dni, nombre, notas))

print(lista_estudiantes)