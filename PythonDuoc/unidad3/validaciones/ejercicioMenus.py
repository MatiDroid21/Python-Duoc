import os
import time

os.system("cls")

menu = True
while menu: 
    print("Sistema Bancos y Asociados")
    print("op1. Paga Tu Tarjeta :3")
    print("op2. Simule Una Compra :3")
    print("op3. Salir")

    opcion = 0
    try:
        opcion = int(input("Ingrese una de las opciones disponibles >> "))
    except:
        print("Error: Se esperaba un numero. Por favor eliga una de las opciones disponibles")

    if opcion < 1 or opcion > 4:
            print("La opción ingresada no es valida. Intente nuevamente")
            time.sleep(1)
            os.system("cls")
    else:
            menu = False

deuda = 100000
pagoDeuda = 0
#validar el input
if opcion == 1:
    print("Posees una deuda de $100.000")
        
    while pagoDeuda < deuda:
        try:
            pagoDeuda += int(input("Ingrese monto a pagar > "))
        except:
            print("Error: Se esperaba un numero. Por favor eliga una de las opciones disponibles")
        
        if pagoDeuda < deuda:
            print(f"Aún le faltan > ${deuda - pagoDeuda}")
        elif pagoDeuda > deuda:
            print(f"Has pagado más. Se te devuelve {pagoDeuda - deuda}")
            
elif opcion == 2:
    print("vas a simular una compra")

    simulacion = True

   # while simulacion:
        
elif opcion == 3:
     print("Fin de ejecucion")
    

   
    
