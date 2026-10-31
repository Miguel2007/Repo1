def inv(lst):
    lst2 = []
    for i in range(len(lst)-1,-1,-1):
        lst2.append(lst[i])
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
lst1.pop(len(lst1)-1)
print(lst1)
print(inv(lst1))
