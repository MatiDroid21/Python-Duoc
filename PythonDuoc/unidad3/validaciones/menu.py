import os
import time #libreria para esperar x tiempo
os.system("cls")

menu = True
while menu:
    print("=== MENU ===")
    print("1. Porotos con riendas \t $5.000clp")
    print("2. Cancato \t\t $8.000clp")
    print("3. Fideos Boloñesa \t $5.500clp")
    print("4. Pollo Arvejado \t $6.000clp")

    try:
        opcion = int(input("Ingresa una de las opciones que se muestra en pantalla > "))
        if opcion < 1 or opcion > 4:
            print("La opción ingresada es incorrecta. Por favor ingrese una de las opciones disponibles.")
            time.sleep(1) #esperar 1 segundo.
            os.system("cls") # si se cae que limpie    
        else:
            menu = False
    except:
        print("Se ingreso algo na que ver, debe ser numero")
        time.sleep(1)
        os.system("cls")

#validar
if opcion == 1:
    print("Usuario seleccionó. Porotos con riendas ")
elif opcion == 2:
    print("Usuario seleccionó Cancato")
elif opcion == 3:
    print("Usuario seleccionó Fideos Boloñesa")
elif opcion == 4:
    print("Usuario seleccionó. Pollo Arverjados")