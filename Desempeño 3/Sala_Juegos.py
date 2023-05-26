edad=int(input("Ingrese la edad del infante: "))

if edad < 4:
    print("El niño puede entrar gratis")
elif edad ==4 or edad<18:
    print("El chico tiene entre 4 y 18 años, page $85.00")
elif edad>=18:
    print("El chic@ ya es mayor o igual de 18 años, pague $150.00")