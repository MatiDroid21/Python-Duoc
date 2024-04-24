import os
import random
import time
os.system("cls")

seleccion = ""
seleccion_pc = ""

puntaje_usuario = 0
puntaje_pc = 0

confirmacion = ""

while confirmacion != 0:
    menu = True
    while menu:
        print("Cachipun")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")

        opcion = 0
        try:
            opcion = int(input("Ingrese una de las opciones disponibles >> "))
        except:
            print("Error: Se esperaba un numero. Por favor eliga una de las opciones disponibles")

        if opcion < 1 or opcion > 3:
                print("La opción ingresada no es valida. Intente nuevamente")
                time.sleep(1)
                os.system("cls")
        else:
            menu = False

    #ver la opcion del pc
    opcion_pc = random.randint(1,3)

    #validamos la opcion del usuario
    if opcion == 1:
        seleccion = "Usuario seleccionó. Piedra"
    elif opcion == 2:
        seleccion = "Usuario seleccionó. Papel"
    elif opcion == 3:
        seleccion = "Usuario seleccionó. Tijeras"
    else:
        print("Seleccion del usuario no valida")

    #validamos la opcion del pc
    if opcion_pc == 1:
        seleccion_pc = "PC seleccionó. Piedra"
    elif opcion_pc == 2:
        seleccion_pc = "PC seleccionó. Papel"
    elif opcion_pc == 3:
        seleccion_pc = "PC seleccionó. Tijeras"
    else:
        print("Seleccion del pc no valida")

    os.system("cls")

    print("Validando.")
    time.sleep(1)
    print("Validando..")
    time.sleep(1)
    print("Validando...")
    time.sleep(1)
    print("Un momento....")

    if opcion == 1 and opcion_pc == 3 or opcion == 2 and opcion_pc == 1 or opcion == 3 and opcion_pc == 2:
        puntaje_usuario += 1
        puntaje_pc += 0
        print(f"Juego ganado - {seleccion} y {seleccion_pc} -- puntaje usuario: {puntaje_usuario} - puntaje pc: {puntaje_pc}")    
    elif opcion == 3 and opcion_pc == 1 or opcion == 1 and opcion_pc == 2 or opcion == 2 and opcion_pc == 3:
        puntaje_pc += 1
        puntaje_usuario += 0
        print(f"Juego perdido - {seleccion} y  {seleccion_pc} -- puntaje usuario: {puntaje_usuario} - puntaje pc: {puntaje_pc}") 
    elif opcion == opcion_pc:
        puntaje_pc += 0
        puntaje_usuario += 0
        print(f"Juego empatado - {seleccion} y {seleccion_pc} -- puntaje usuario: {puntaje_usuario} - puntaje pc: {puntaje_pc}")

    #validar la confirmacion de volver a jugar.        
    try:
        confirmacion = int(input("Desea jugar otra vez? 1. Si 0. No >> "))
        if confirmacion < 0 or confirmacion > 1:
            print("La opción ingresada no es valida. Intente nuevamente")
            time.sleep(1)
            confirmacion = int(input("Desea jugar otra vez? 1. Si 0. No >> "))
            os.system("cls")

        if confirmacion == 1:
                os.system("cls")
        elif confirmacion == 0:
                os.system("cls")
                print("Gracias por jugar")
        else:
                print("Opcion no valida. Intente nuevamente")
    except:
        print("Error: Se esperaba un numero. Por favor eliga una de las opciones disponibles")