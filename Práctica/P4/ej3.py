j = 0
lst = -1
lst1 = []

while lst != 0:
    if j == 0 and lst != 0: 
        lst = int(input("Introduzca los valores de la lista(0 para terminar): "))
        lst1.append(lst)
        j += 1
    elif lst != 0:
        lst = int(input())
        lst1.append(lst)

def suma(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum


print("La suma de los elementos es:", suma(lst1))