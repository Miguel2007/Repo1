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
solicitud = ""
i = 0
terminar = False

while solicitud.upper() != 'S' and solicitud.upper() != 'N':
    solicitud = input("¿Desea modificar los datos de algun alumno?(S/N): ")
    if solicitud.upper() != 'S' and solicitud.upper() != 'N':
        print("Introduzca una solicitud válida(S/N).")

if solicitud.upper() == 'S':
    id = input("Introduzca el DNI del alumno para modificar sus datos: ")

    while i < len(lista_estudiantes) and terminar == False:
        if id == lista_estudiantes[i]["DNI"]:
            data = input("Introduce que tipo de dato deseas cambiar(dni, nombre o notas): ")

            if data == 'dni':
                n_dni = input("Introduce el nuevo DNI: ")
                lista_estudiantes[i].update({"DNI": n_dni})
            elif data == 'nombre':
                n_nombre = input("Introduzca el nuevo nombre: ")
                lista_estudiantes[i].update({"Nombre": n_nombre})
            elif data == 'notas':
                fin = False
                n_notas = []

                while fin == False:
                    n_nota = int(input("Introduzca las nuevas notas(-1 para acabar): "))
                    if n_nota != -1:
                        n_notas.append(n_nota)
                    elif n_nota == -1:
                        fin = True
                        lista_estudiantes[i].update({"Notas": n_notas})
            terminar = True

    
        
        else:
            print(f"No existe alumno con el DNI: {id}")

        

        print(f"El alumno modificado quedaría así: {lista_estudiantes[i]}")
        print(f"Tabla completa: {lista_estudiantes}")
        i += 1
        

elif solicitud == 'N':
    print("Exit.")

