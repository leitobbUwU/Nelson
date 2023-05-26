class Clientes:
    cNombre = None
    cAp = None
    cAm = None
    cEdad = 0
    cFechaN = None
    cRFC = None
        
    def __init__(self):
        print("Registro de cliente")
    
    def registrarCliente(self, n, ap, am, e, fn, rfc):
        self.cNombre = n
        self.cAp=ap
        self.cAm=am
        self.cEdad=e
        self.cFechaN=fn
        self.cRFC=rfc
        print("Se ha registrado coerrectamente el cliente.")
        
    def mostrarCliente(self):
        print("El cliente registrasdo es:\n Nombre del cliente: ",self.cNombre,"\n"
              ,"Apellido Paterno del cliente: ",self.cAp,"\n"
              ,"Apellido Materno del cliente: ",self.cAm,"\n"
              ,"Edad del cleinte: ",str(self.cEdad),"\n"
              ,"Fecha de nacimiento del cliente: ",self.cFechaN,"\n"
              ,"RFC del cleinte: ",self.cRFC)
        
    def __del__(self):
        print("El cliente ",self.cNombre,self.cAp," ",self.cAm," se está eliminando......")
    
nombre = input("Ingres a el nombre del cliente: ")
aps=input("Ingrese el apellido paterno del cliente: ")
ams=input("Ingrese el apellido materno del cliente: ")
edad=int(input("Ingrese la edad del cliente: "))
fechaN=input("Ingrese la fecha de nacimiento del cliente: ")
rfcs=input("Ingrese el RFC del cliente: ")

#Instancia de clase
cliente_1=Clientes()

cliente_1.registrarCliente(nombre, aps, ams, edad, fechaN, rfcs)
cliente_1.mostrarCliente()
#Se elimina el objeto
del(cliente_1)