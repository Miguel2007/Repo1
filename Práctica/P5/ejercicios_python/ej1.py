print("Introduce los datos del alumno:\n" )

def datos(dni, nombre, notas):

    estudiante = {}
    estudiante.update({"DNI": dni, "Nombre": nombre, "Notas": notas})
    
    return estudiante

    
dni = input("DNI: ")
nombre = input("Nombre: ")
fin = False
notas = []

while fin == False:

    nota = int(input("Notas(-1 para terminar): "))
    if nota != -1:
        notas.append(nota)
    if nota == -1:
        print(datos(dni, nombre, notas))


