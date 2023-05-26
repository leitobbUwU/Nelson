contraseña=("sistemas2023")
Validar=input("Ingrese la contraseña para ingresar: ")
va=Validar.lower()

while True:
    if contraseña==va:
        print("La contraseña es correcta :)")
        break
    else:
        print("La contraseña es incorrecta :(")
        Validar=input("Ingrese la contraseña nuevamente: ")
        va=Validar.lower()
    