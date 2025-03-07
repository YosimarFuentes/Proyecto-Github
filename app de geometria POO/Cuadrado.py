class Cuadrado:
  #constructor
    def __init__(self,lado):
      self.lado = lado
#Metodos

    def calcular_area(self):
        return self.lado ** 2 
    
    def calcular_perimetro(self):
        return 4*self.lado
    
    def menu(self):
        print("El area del Cuadrado es:", self.calcular_area())
        print("El perimetro del Cuadrado es:", self.
        calcular_perimetro())
  