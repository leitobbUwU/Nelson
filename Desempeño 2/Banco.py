cantidad=float(input("Ingrese la cantidad a ahorrar: "))
c=str(cantidad)

multiplicar=round(cantidad+(cantidad*.10), 2)
multiplicar1=(round(cantidad+(cantidad*.10), 2))*2
multiplicar2=(round(cantidad+(cantidad*.10), 2))*3

m=str(multiplicar)
m2=str(multiplicar1)
m3=str(multiplicar2)

print("La cantidad ahorrada fue: "+ c +" La cantidad del primer año fue: "+m+
      " La cantidad del segundo año fue: "+m2+" La cantidad del tercer año fue: "+m3)