class Rectangulo:
    def __init__(self,b,h):
        self.base=b
        self.altura=h
        
    def baseRec(self, bas):
        self.base = bas
        print("La base es: ",bas)
        
    def alturaREc(self, alt):
        self.altura=alt
        print("La altura es: ",alt)
    
    def area(self,bas,alt):
        self.b = bas
        self.h=alt
        area=bas*alt
        a=str(area)
        print("El area es: ",a)
        
    def perimetro(self,lado,lado2):
        self.b = lado
        self.h=lado2
        perimetro=(lado+lado2)*2
        p=str(perimetro)
        print("El perimetro es: ", p)
    
base=int(input("Ingrese el largo de la base: "))
altura=int(input("Ingrese la altura del lado: "))

rectangulo_1=Rectangulo(base, altura)
rectangulo_1.baseRec(base)
rectangulo_1.alturaREc(altura)
rectangulo_1.area(base,altura)
rectangulo_1.perimetro(base,altura)