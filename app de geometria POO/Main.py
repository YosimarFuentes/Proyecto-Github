
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from triangulo import triangulo

val= True
while val==True:
    print("Menu Principal, Figuras Geometricas")

    print("1: Cuadrado")
    print("2: Regtangulo")
    print("3: Triangulo")
    print("4: Salir")

    opcion= int(input("Digite una opcion: "))
    print("")
    
    if opcion == 1:
        print("Bienvenido a Cuadrado")
        print("Elaboremos el objeto del Cuadrado")
        lado=int (input("Digite el lado del Cuadrado para crear el objeto: "))
        #instancia del objeto Cuadrado
        miCuadrado=Cuadrado(lado)
        #llamo a mi menu cuadrado
        miCuadrado.menu()
        print("")
        print("")

        
    elif opcion == 2:
        print
        print("Bienvenido a Rectangulo")
        print("Elaboremos el objeto del Rectangulo")
        base=int (input("Digite la base del Rectangulo para crear el objeto: "))
        altura=int (input("Digite la altura del Rectangulo para crear el objeto: "))
        #instancia del objeto Rectangulo
        miRectangulo=Rectangulo(base,altura)
        #llamo a mi menu Rectangulo
        miRectangulo.menu()
        print("")
        print("")
        
    elif opcion == 3:
        print
        print("Bienvenido a Triangulo")
        print("Elaboremos el objeto del Triangulo")
        base=int (input("Digite la base del Triangulo para crear el objeto: "))
        altura=int (input("Digite la altura del Triangulo para crear el objeto: "))
        lado1=int (input("Digite el lado1 del Triangulo para crear el objeto: "))
        lado2=int (input("Digite el lado2 del Triangulo para crear el objeto: "))
        
        #instancia del objeto
        mitriangulo=triangulo(base,altura,lado1,lado2)
        #llamo a mi menu 
        mitriangulo.menu()
        print("")
        print("")
        
        
    elif opcion == 4:
        val=False
    elif opcion != 1 and 2 and 3 and 4:
        print("Error opcion valida")
        print("Gracias por preferirnos")



   
