notas = {
    'Luis': 5.3,
    'Ana': 6.4,
    'Juan': 4.1
}

dic = notas

nombre = input("Introduzca un nombre para consultar su nota: ")

n = 0
m = 0
for name in dic:
    if nombre in dic and n == 0:
        print(dic[nombre])
        n += 1
    if nombre not in dic and m == 0:
        print(f"'{nombre}' no aparece en la lista.")
        m += 1