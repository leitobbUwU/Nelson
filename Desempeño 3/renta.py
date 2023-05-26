renta=float(input("ingrese su renta anual: "))

if renta<5000:
    impositivo=renta+(renta*.05)
    i=str(impositivo)
    print("Por pagar menos de 5000 paga: " + i)
elif renta==5000 or renta<10000:
    impositivo=renta+(renta*.15)
    im=str(impositivo)
    print("Por pagar entre 5000 y 10000 paga: " + im)
elif renta==10000 or renta<25000:
    impositivo=renta+(renta*.25)
    imp=str(impositivo)
    print("Por pagar entre 10000 y 25000 paga: " + imp)
elif renta == 25000 or renta<50000:
    impositivo=renta+(renta*.30)
    impo=str(impositivo)
    print("Por pagar entre 25000 y 50000 paga: " + impo)
elif renta > 50000:
    impositivo=renta+(renta*.45)
    impos=str(impositivo)
    print("Por pagar mas de 50000 paga: " + impos)
else:
    print("Ingrese una cantidad valida")