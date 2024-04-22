import os
import time

#menu 3 opciones. 
opcionMenu = 0
deuda = 100000
pago = 0 #var que voy a usar para la pagar la deuda
compra = 0 #var que voy a usar para comprar
respuesta = ""
while opcionMenu != 3:
    os.system("cls")
    print("=== Menu De Banco Fantasia ===")
    print("1. Pagar Deuda De Tarjeta")
    print("2. Simulación De Compras")
    print("3. Salir")
    try:
        opcionMenu = int(input("Ingrese Opcion > "))
        if opcionMenu < 1 or opcionMenu > 4:
            print("Debes seleccionar una de las opciones disponibles.")
            time.sleep(2)
    except:
       print("Se esperaba un numero")
       time.sleep(2)
    
    if opcionMenu == 1:
        #pagar deuda
        while deuda != 0:
            print(f"Usted tiene una deuda de ${deuda}")
            try:
                pago = int(input("Ingrese monto a pagar > $"))
            except:
                print("Se esperaba un numero")
     
            while pago < 1 or pago > deuda:
                print("Error: El monto ingresado es no corresponde a lo adeudado")
                time.sleep(2)
                try:
                    pago = int(input("Ingrese monto a pagar > $"))
                except:
                    print("Se espera un numero")
            deuda = deuda - pago 
            print(f"Falta por pagar {deuda}") 
            time.sleep(2)
            os.system("cls")   
    elif opcionMenu == 2:
        #simulacion de compras
        while respuesta != "no":
                try:
                    compra = int(input("Ingrese Monto A Comprar >> "))
                    while compra < 0:
                        compra = int(input("Ingrese Monto A Comprar >> "))
                    deuda = deuda + compra
                    print(f"Llevas un adeudado de {deuda}")
                    respuesta = input("Quieres seguir comprando si/no >> ")
                except:
                    print("Se esperaba un numero")
    elif opcionMenu == 3:
        print("Fin Del Programa...")
        time.sleep(2)



