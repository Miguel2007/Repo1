num = -1
num1 = []
max = 0




while num != 0:
    num = float(input("Introduzca el número: "))
    num1.append(num)
    for i in range(len(num1)):
        if num1[i] > max:
            max = num1[i]
        else:
            max = max
print("El número más grande es", max)
