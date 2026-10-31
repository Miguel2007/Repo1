ent = int(input("Introduzca un número entero: "))

if ent % 3 == 0 and ent % 5 == 0:
    print(ent, "es divisible entre 3 y 5.")

elif ent % 3 != 0 and ent % 5 != 0:
        print(ent, "no es divisible entre 3 ni 5.")

elif ent % 3 != 0:
        print(ent, "no es divisible entre 3.")
        
elif ent % 5 != 0:
        print(ent, "no es divisible entre 5.")

    