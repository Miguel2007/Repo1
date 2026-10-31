con = 0
con = input("Introduzca la contraseña: ")
while con != 'secreta123':
    print("Acceso denegado.")
    con = input("Introduzca la contraseña: ")

else: 
    print("Acceso concedido.")
    
