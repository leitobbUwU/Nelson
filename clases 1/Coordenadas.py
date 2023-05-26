import numpy as np


class Punto:        
    def __init__(self):
        # self.cordx=cox
        # self.cordy=coy
        # if cox=="" and coy=="":
        #     cox=0
        #     coy=0
        pass
            
    def imprimirCoordenada(self, cx, cy):
        self.coordenadaX=cx
        self.coordenaday=cy
        print("(",self.coordenadaX,",",self.coordenaday,")")
        
    def cuadrante(self, cx, cy):
        if cx==0 and cy!=0:
            print("El punto se encuentra el en eje Y")
        elif cx!=0 and cy==0:
            print("El punto se encuentra en el cuadrante X")
        elif cx==0 and cy==0:
            print("El punto se encuentra sobre el origen")
            
    def distancia(self,cx,cy):
        self.coordenadaX=cx
        self.coordenaday=cy
        cordeny=int(cy)
        cordenx=int(cx)
        cordenx2=int(input("Ingrese otro punto X:"))
        cordeny2=int(input("Ingrese otro punto Y: "))
        cuadrado=((cordenx2-cordenx)**2)+((cordeny2-cordeny)**2)
        raiz=np.sqrt(cuadrado)
        print("La raiz es: ",raiz)
                    
cordx=int(input("Ingrese la coordenada X: "))
cordy=int(input("Ingrese la coordenada Y: "))

punto_1=Punto()

punto_1.imprimirCoordenada(cordx,cordy)
punto_1.cuadrante(cordx,cordy)
punto_1.distancia(cordx,cordy)

