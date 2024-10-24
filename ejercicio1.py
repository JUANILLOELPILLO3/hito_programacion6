def enseñar_cuadrado():#creammoas una funcion la cual llamaremos mas tarde
    lado = int(input("dame las medidas de sus lados"))#pedimos al usuario q introduzca medidas
    area = lado * lado#fomulas del area y del perimetro
    perimetro = lado + lado + lado + lado
    for a in range(lado):
        print("* " * lado) #creamos un bucle para que los asteriscos se produzcan = al numero de lados
    print(f"el area es: {area} cm" )
    print(f"el perimetro es: {perimetro}")    

def enseñar_rectangulo():
    base = int(input("dame el ancho del rectángulo: "))
    altura = int(input("dame la altura del rectángulo: "))
    area = base * altura
    perimetro = 2* (base + altura)
    for a in range(altura):
        print("* " * base)
    print(f"el area es: {area} cm")  
    print(f"el perimetro es: {perimetro}")  

while True:# llamamos a las dos funciones y haremos que el usuario pueda elegir cual llama con 1 o 2 de tal forma que en funcion del numero que elija llamara a una o otra
    print("elige una de las opciones:")
    print("1 Cuadrado")
    print("2 Rectangulo")
    opcion = input("¿cual eliges? (1 o 2): ")
    if opcion == "1":
        enseñar_cuadrado()
        break
    elif opcion == "2":
        enseñar_rectangulo()
        break
    else:
        print("elige 1 o 2.")
