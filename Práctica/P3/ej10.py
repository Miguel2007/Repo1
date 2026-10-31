def med(sum, n):
    media = sum / n
    return media

def var(sum, n, suma):
    
    varianza = (sum / n) - (suma / n)**2
    
    return varianza

def des(var):
    desviacion = var**0.5
    return desviacion

num = -1
num1 = []
suma = 0
suma2 = 0
i = 0

while num != 0:
    if i != 0:
        num = float(input(""))
    else:
        num = float(input("Introduzca el número(para terminar 0):\n"))
    if num != 0:
        num1.append(num)
    i += 1
for i in range(len(num1)):
    suma += num1[i]
    suma2 += num1[i]**2

media = med(suma, len(num1))
varianza = var(suma2, len(num1), suma)
desviacion = des(varianza)
print("La media es:", media)
print("La varianza es:", varianza)
print("La desviación típica es:", desviacion)