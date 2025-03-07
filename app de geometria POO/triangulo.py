class triangulo:
  #constructor
  def __init__(self,lado1,lado2,base,altura):
      self.lado1 = lado1
      self.lado2 = lado2
      self.base = base
      self.altura = altura
       
#Metodos
  def calcular_area(self):
     return (self.base * self.altura) / 2
     
  def calcular_perimetro(self):
        return  self.lado1 + self.lado2 + self.base
    
  def menu(self):
        print("El area del Triangulo es:", self.calcular_area())
        print("El perimetro del Triangulo es:", self.calcular_perimetro())
  