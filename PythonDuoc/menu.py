import os
import time

os.system("cls")

nombre_abarrote = ""
valor_abarrote = ""

#acumuladores
cantidad_fideos = 0
cantidad_salsa = 0
cantidad_arroz = 0
cantidad_aceite = 0

menu_general = True

while menu_general:
    print("=== SUPERMERCADO ===")
    print("1. Abarrotes")
    print("2. Carniceria")
    print("3. Limpieza")
    print("4. Boleta/Pago")
    print("5. Finalizar Programa")

    opcion_general = 0
    try:
        opcion_general = int(input("Ingrese una opción"))
    except:
        print("Se esperaba un número...")
    
    if opcion_general == 1:
        menu_abarrotes = True
        while menu_abarrotes: 
            print("=== Menú Abarrotes ===")
            print("1. Fideos Carozzi $700 c/u")
            print("2. Salsa de tomates $500 c/u")
            print("3. Arroz $1000 c/u")
            print("4. Aceite maravilla $3000 c/u")
            print("5. Devolver a menú principal")

            opcion_abarrotes = 0
            try:
                opcion_abarrotes = int(input("Ingrese una opción"))
            except:
                print("Se esperaba un número...")

            if opcion_abarrotes < 1 or opcion_abarrotes > 5:
                print("La opción ingresada no es correcta o no está disponible.")
                time.sleep(2)
                os.system("cls")
            else:
                if opcion_abarrotes == 1:
                    cantidad_fideos += int(input("Ingrese la cantidad de paquetes de fideos a comprar"))
                elif opcion_abarrotes == 2:
                    cantidad_salsa += int(input("Ingrese la cantidad de salsas de tomates a comprar"))
                elif opcion_abarrotes == 3:
                    cantidad_salsa += int(input("Ingrese la cantidad de paquetes de arroz a comprar"))
                elif opcion_abarrotes == 4:
                    cantidad_salsa += int(input("Ingrese la cantidad de botellas de aceites a comprar"))
                elif opcion_abarrotes == 5:
                    os.system("cls")
                    menu_abarrotes = False
                else:
                    print("Opción No disponible")
    elif opcion_general == 4:
        print("=== BOLETA ===")
        print("     Cantidad           || Producto           || Valor Unitario  || Total")
        print(f"  {cantidad_fideos}     || Fideos             ||      $700       || ${cantidad_fideos * 700}")
        print(f" {cantidad_salsa}      || Salsa De Tomate    ||      $500       || ${cantidad_salsa * 500}")
        print(f" {cantidad_arroz}      || Arroz              ||      $1000      || ${cantidad_arroz * 1000}")
        print(f"  {cantidad_aceite}     || Aceite             ||      $3000      || ${cantidad_aceite * 3000}")
        print("=========================================================")
        print(f"Total: ${(cantidad_fideos*700 + cantidad_salsa * 500 + cantidad_arroz * 1000 + cantidad_aceite * 3000)}")
        menu_general = False
    elif opcion_general == 5:
        os.system("cls")
        menu_general = False   
    else:
        print("Opcion ingresada es incorrecta")         
