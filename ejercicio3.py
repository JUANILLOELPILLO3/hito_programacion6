total = 0
while True:
    cliente = float(input("introduce el saldo de tu cuenta"))
    if cliente >0: 
        total =cliente
        print(f"El saldo de tu cuenta es: {total}")
        break
    else:
        print("introduzca una cantidad de saldo positiva")

while True:
    print("aqui tienes todas las opciones escoge la que deses realizar\n\
    1.- ingresar dinero:\n\
    2.- sacar dinero: \n\
    3.- mostrar saldo: \n\
    4.- salir:\n")      
    opcion=int(input())
    if opcion== 1:
        ingreso=float(input("¿cuanto dinero vas a imgresar?"))
        total+=ingreso
        print(f"tu nuevo saldo es:{total}")
    elif opcion== 2:
        retirar=float(input("¿cuanto quieres retirar?"))
        if total-retirar<0:
            print("no tienes tanto dinero")
        else:
         total-=retirar
         print(f"tu nuevo saldo es {total}")
    elif opcion== 3:
        mostrar_saldo=print(f"tu saldo es{total} ")
    elif opcion== 4:
        print("espero que este conforme con su visita,!hasta la proxima!")
        break
    else:
        print("no dispongo de ese programa porfavor ingrese un numero del 1 al 4")
