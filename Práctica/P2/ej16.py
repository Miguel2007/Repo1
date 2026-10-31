rent = float(input("Introduzca su renta anual (€): "))

if rent < 10000:
    print("Tipo impositivo del 5%.")
elif rent >= 10000 and rent <= 19999.99:
    print("Tipo impositivo del 15%.")
elif rent >= 20000 and rent <= 34999.99:
    print("Tipo impositivo del 20%.")
elif rent >= 35000 and rent <= 59999.99:
    print("Tipo impositivo del 30%.")
elif rent >= 60000:
    print("Tipo impositivo del 45%.")