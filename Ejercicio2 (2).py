import random # sacanos la opcion ranndom de la bilbioteca para usarlo mas tarde 

lista = ['piedra', 'papel' , 'tijera']
victorias_jugador = 0 # las victorias del jugador
victorias_equipo = 0 # las victorias de la maquina

while victorias_jugador < 2 and victorias_equipo < 2:#cuando uno llega a dos se acaba el juego
    jugador= None# jugador es igual a nada
    equipo=random.choice(lista) # elige una opcion aleatoria de la lista

    while jugador not in lista:
        jugador = input("elige: piedra,papel o tijera:").lower()# idicamos al jugador los diferentes sucesos que puede seguir
    if jugador == equipo:
            print( f'equipo:', equipo) 
            print(f'jugador:', jugador)
            print('empate')    
    elif jugador == 'piedra':
        if equipo == 'papel':
            print( 'equipo:', equipo) 
            print('jugador:', jugador)
            print('has perdido')
            victorias_equipo += 1 # se añade una victoria a la maquina
        if equipo == 'tijera':
            print( 'equipo:',equipo) 
            print('jugador:', jugador)
            print('has ganado')
            victorias_jugador += 1  # se añade una victoria al jugador
    elif jugador == 'papel':
        if equipo == 'tijera':
            print('equipo:', equipo) 
            print('jugador:', jugador)
            print('has perdido')
            victorias_equipo += 1 
        if equipo == 'piedra':
            print( 'equipo:', equipo) 
            print('jugador:', jugador)
            print('has ganado')
            victorias_jugador += 1
    elif jugador == 'tijera':
        if equipo == 'piedra':
            print('equipo:', equipo) 
            print('jugador:', jugador)
            print('has perdido')
            victorias_equipo += 1 
        if equipo == 'papel':
            print('equipo:', equipo) 
            print('jugador:', jugador)
            print('has ganado')
            victorias_jugador += 1
    print(f'Marcador: Jugador {victorias_jugador} - Equipo {victorias_equipo}')#le damos la orden de mostrar el marcador depues de cada tirada
if victorias_jugador == 2:# una vez alcanzado las victorias indicamos que muestre cualquiera de los dos sucesos posibles
        print("has ganago el juego")
else:
        print("El equipo ha ganado el juego al mejor de 3.")

    

