global saldo
saldo=40000

def pedirU():
    usuario=input("Ingrese usuario: ")
    return usuario

def pedirC():
    contra=input("Ingrese contraseña: ")
    return contra

def menu(opcion, saldo):
    if opcion==1:
        restar=int(input("Ingrese la cantidad a retirar: "))
        disminuir=saldo-restar
        saldo=disminuir
        print("El nuevo saldo es: $", saldo)
                    
    elif opcion==2:
        aumentar=int(input("Ingrese la cantidad a depositar: "))
        aumentar=saldo+aumentar
        saldo=aumentar
        print("La nueva cantidad es: $", aumentar)
                    
    elif opcion==3:
        print("La cantidad actual es: $", saldo) 

def main():
    usuario1=("Admin")
    contra1=("Admin")
    intento=0
    while intento < 3:
        if pedirU()==usuario1 and pedirC()==contra1:
            print("Bienvenido")
            Veces=int(input("¿Cuantas veces se repetira?: "))
            cantidad=int(40000)
            con=1
                    
            while con<=Veces:
                con=con+1
                print("1.- Retirar")
                print("2.- Depositar")
                print("3.- Corte")
                        
                opcion=int(input("Ingrese la operación a realizar: "))
                        
                menu(opcion, cantidad)
            
        else:
            intento = intento + 1
            print("Llevas " , intento ," intentos")# usuario==usuario1 and contra==contra1:
            
    print("Bienvenido")
    Veces=int(input("¿Cuantas veces se repetira?: "))
    con=1
            
    while con<=Veces:
        con=con+1
        print("1.- Retirar")
        print("2.- Depositar")
        print("3.- Corte")
                
        opcion=int(input("Ingrese la operación a realizar: "))
                
        menu(opcion, saldo)
                          
        
if __name__=="__main__":
    main()