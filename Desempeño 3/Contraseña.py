contraseña=input(("Ingrese la contraseña: "))

contraseña2=input("Vuelva a ingresar la contraseña: ")

c1=contraseña.lower()
c2=contraseña2.lower()

while contraseña!=contraseña2:
    if c1==c2:
        print("La contraseña coincide")
        
    else:
        print("Las contraseñas no coinciden :c")
        break