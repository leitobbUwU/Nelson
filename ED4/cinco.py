cantidad=input("Ingrese la cantidad a invertir: ")
interes=input("Ingrese el interes: ")
duracion=input("Ingrese los años: ")

i=int(interes)
d=int(duracion)

for i in range (1, d+1):
    inter=i*0.10
    capital=inter*d
    print(i)

cv=int((cantidad)[::-1])
print(cv)