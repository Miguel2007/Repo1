def mostrar_diccionario(dic):
    j = 0
    k = 0

    print("\n")
    print("Claves: ")
    for i in dic.keys():
        print(f"La clave {j} es: {i}.")
        j += 1
    print("\n")
    print("Valores: ")
    for i in dic.values():
        print(f"El valor {k} es: {i}.")
        k += 1

    print("\n")
    print("Diccionario entero: ")
    for i, el in dic.items():
        
        print(i, el)

    

precios = {
    "Pera" : 1,
    "Manzana" : 0.5,
    "Limón" : 1.2,
    "Mango" : 2,
    "Piña" : 3

}

print(mostrar_diccionario(precios))