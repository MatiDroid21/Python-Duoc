import os
os.system("cls")

tablero = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] #para mostrar el tablero

jugador = "X"


elecciones_X = []
elecciones_O = []

def mostrarTablero():
    os.system("cls")
    print("=== GATO ===")
    t = ""
    for fila in tablero:
        for numero in fila:
            #dibujar tablero
            if numero in elecciones_X:
                t += f"| X"
            elif numero in elecciones_O:
                t += f"| O"
            else:
                t += f"| {numero} "    
        t+="| \n"
    print(t)        

def elegirOpcion(jugador):
    
    opcion = int(input(f"Jugador {jugador} Ingresa una opcion >> "))
    
    if opcion in elecciones_X or opcion in elecciones_O:
        input("Esa opción ya fue ocupada. Presione Enter para continuar")
    else:
        if jugador == "X":
            elecciones_X.append(opcion)
            #jugador = "O"
        else:
            elecciones_O.append(opcion)
            #jugador = "X"
        return opcion    
    
def jugadorGanador():
    # combinaciones ganadoras
    combinaciones_ganadoras = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # filas
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columnas
        [1, 5, 9], [3, 5, 7]              # diagonales
    ]

    for combinacion in combinaciones_ganadoras:
        if all(elem in elecciones_X for elem in combinacion):
            print("Jugador X gana!")
            return True
            break
        if all(elem in elecciones_O for elem in combinacion):
            print("Jugador O gana!")
            return True
            break
    return False

ganador = False

#esto seria una especie de main()
while ganador ==  False:
    mostrarTablero()
    jugadorGanador()
    elegirOpcion(jugador)
    
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"


