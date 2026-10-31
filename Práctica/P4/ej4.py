num = input("Introduzca números enteros positivos separados por ',': ")
max = -99999
num = num.split(',')

for i in range (len(num)):
    if int(num[i]) > max:
        max = int(num[i])
print("El número más grande es:", max)
