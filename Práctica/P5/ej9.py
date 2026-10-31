compra = {}
articulo = ""
fin = False

while fin == False:
    articulo = input("Introduzca el producto(fin para terminar): ")
    if articulo =='fin':
        fin = True

    elif fin == False:
        precio = float(input("Introduzca el precio del producto: "))
        compra.update({articulo: precio})


print("\n")
print("Lista de la comopra:")

for i, producto in compra.items():
    print(i, producto)
print("\n")