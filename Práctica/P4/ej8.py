lista_numeros = [1, 2, 3, 4 ,5]
i = 0
intentos = 0
fallos = 0
aciertos = 0
final = True
while i < len(lista_numeros) and final == True:
    adiv = int(input("Adivina los números(0-10), tienes 5 intentos: "))

    if intentos > 4:
        final = False
    
    elif adiv in lista_numeros:
        print("El número", adiv, "está en la lista.")
        i += 1
        intentos += 1
        aciertos += 1

    elif adiv not in lista_numeros:
        print("El número", adiv, "no está en la lista.")
        intentos += 1
        fallos += 1

    elif adiv > 10 and adiv < 0:
        print("Valor fuera de rango.")
        intentos += 1
        fallos += 1

if aciertos == len(lista_numeros):
    print("Has adivinado todos los números de la lista:", lista_numeros)
    print(f"Aciertos: {aciertos}, fallos: {fallos}")
else:
    print("Has superado el número de intentos.")
    print(f"Aciertos: {aciertos}, fallos: {fallos}")