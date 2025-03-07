class Rectangulo:
  #constructor
  def __init__(self,base,altura):
      self.base = base
      self.altura = altura  
#Metodos
  def calcular_area(self):
     return self.base * self.altura
    
  def calcular_perimetro(self):
        return  (self.base + self.altura) *2
      
  def menu(self):
      print("El area del Rectangulo es:", self.calcular_area())
      print("El perimetro del Rectangulo es:", self.calcular_perimetro())
      