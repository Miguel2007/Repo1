coste_kg = {
    "Pera": 3,
    "Manzana": 2.3,
    "Kiwi": 1.3,
    "Mango": 4.5,
    "Plátano": 2.7,
    "Uvas": 3.3,
    "Níspero": 3.1,
}


final = False
suma = 0

while final == False:
    fruta = input("Introduzca la fruta(fin para acabar): ")
    if fruta != 'fin':
        peso = float(input("Introduzca la cantidad de fruta(kg): "))

    if fruta == 'fin':
        final = True

    elif fruta in coste_kg:
        print("El precio por kilo de", fruta, "es de", coste_kg[fruta])
        suma += coste_kg[fruta] * peso

    elif fruta not in coste_kg:
        print("La fruta indicada no está en la lista.")

print(f"La cantidad a pagar es de {suma}€.")