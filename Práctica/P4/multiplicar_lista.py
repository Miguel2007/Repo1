def mul_lista(lst,num):
    lst2 = []
    for i in range(len(lst)):
        mult = lst[i] * num
        lst2.append(mult)
    return lst2


lst = 1
lst1 = []
j = 0

while lst != 0:
    if j == 0 and lst != 0: 
        lst = int(input("Introduzca los valores de la lista(0 para terminar): "))
        lst1.append(lst)
        j += 1
    elif lst != 0:
        lst = int(input())
        lst1.append(lst)
num = int(input("Introduzca un valor entero para multiplicar la lista: "))

print("La lista resultante es: ", mul_lista(lst,num))