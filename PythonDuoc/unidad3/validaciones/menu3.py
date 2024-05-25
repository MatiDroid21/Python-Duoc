import os
import time

os.system("cls")

nombre_abarrote = ""
valor_abarrote = ""

#acumuladores abarrotes
cantidad_fideos = 0
cantidad_salsa = 0
cantidad_arroz = 0
cantidad_aceite = 0

#acumuladores limpieza
cantidad_limpiador = 0
cantidad_desinfectante = 0
cantidad_jabon = 0
cantidad_shampoo = 0

menu_general = True

while menu_general:
    print("=== SUPERMERCADO MENU ===")
    print("1. Abarrotes")
    print("2. Limpieza")
    print("3. Carniceria")
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
    elif opcion_general == 2:
        menu_limpieza = True
        print("=== Articulos De Limpieza ===") 
        print("1. Limpiador $1000 c/u")
        print("2. Desinfectante $2000 c/u")
        print("3. Jabon $1500 c/u")
        print("4. Shampoo $1000 c/u")
        print("5. Devolver a menú principal")
        
        opcion_limpieza = 0
        try:
                opcion_limpieza = int(input("Ingrese una opción"))
        except:
                print("Se esperaba un número...")

        ##########
        if opcion_limpieza < 1 or opcion_limpieza > 5:
                print("La opción ingresada no es correcta o no está disponible.")
                time.sleep(2)
                os.system("cls")
        else:
            if opcion_limpieza == 1:
                cantidad_limpiador += int(input("Ingrese la cantidad de limpiadores a comprar"))
            elif opcion_limpieza == 2:
                cantidad_desinfectante += int(input("Ingrese la cantidad de desinfectante a comprar"))
            elif opcion_limpieza == 3:
                cantidad_jabon += int(input("Ingrese la cantidad de paquetes de jabon a comprar"))
            elif opcion_limpieza == 4:
                cantidad_shampoo += int(input("Ingrese la cantidad de botellas de shampoo a comprar"))
            elif opcion_limpieza == 5:
                os.system("cls")
                menu_limpieza = False
            else:
                print("Opción No disponible")

        


    elif opcion_general == 4:
        print("=== BOLETA ===")
        print("     Cantidad             || Producto           || Valor Unitario  || Total")
        print(f"  {cantidad_fideos}      || Fideos             ||      $700       || ${cantidad_fideos * 700}")
        print(f" {cantidad_salsa}        || Salsa De Tomate    ||      $500       || ${cantidad_salsa * 500}")
        print(f" {cantidad_arroz}        || Arroz              ||      $1000      || ${cantidad_arroz * 1000}")
        print(f"  {cantidad_aceite}      || Aceite             ||      $3000      || ${cantidad_aceite * 3000}")
        print("=========================================================")
        print(f" {cantidad_limpiador}    || Limpiador          ||      $1000       || ${cantidad_limpiador * 1000}")
        print(f" {cantidad_desinfectante}|| Desinfectante      ||      $2000       || ${cantidad_desinfectante * 2000}")
        print(f" {cantidad_jabon}        || Jabon              ||      $1500      || ${cantidad_jabon * 1500}")
        print(f" {cantidad_shampoo}      || Shampoo            ||      $1000      || ${cantidad_shampoo * 1000}")
        print("=========================================================")
        print(f"Total: ${(cantidad_fideos*700 + cantidad_salsa * 500 + cantidad_arroz * 1000 + cantidad_aceite * 3000)}")
        print(f"Total: ${(cantidad_limpiador*1000 + cantidad_desinfectante * 2000 + cantidad_jabon * 1500 + cantidad_shampoo * 1000)}")
        menu_general = False
    elif opcion_general == 5:
        os.system("cls")
        menu_general = False   
    else:
        print("Opcion ingresada es incorrecta")   