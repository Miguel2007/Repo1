def rep(lst):
    sin_repetidos = []
    for num in lst:
        if num not in sin_repetidos:
            sin_repetidos.append(num)
        
            
    print(sin_repetidos)
    return sin_repetidos    

lst1 = []
lst = 1
j = 0

while lst != 0:
    if j == 0: 
        lst = int(input("Introduzca los valores de la lista(0 para terminar): "))
        if lst != 0:
            lst1.append(lst)
        j = 1
    else:
        lst = int(input())
        if lst != 0:
            lst1.append(lst)

print("La lista sin valores repetidos queda así:", rep(lst1))
