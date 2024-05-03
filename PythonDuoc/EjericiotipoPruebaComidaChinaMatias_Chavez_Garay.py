import os
import time

#cantidad platillos
cantidad_camaronMandarin = 0
cantidad_carneMongoliana = 0
cantidad_chapsuiPollo = 0
cantidad_chapsuiCarne = 0
cantidad_parrilladaChina = 0

#precios platillos
precio_camaronMandarin = 0
precio_carneMongoliana = 0 
precio_chapsuiPollo = 0 
precio_chapsuiCarne = 0 
precio_parrilladaChina = 0 
confirmar = 0
#
subtotal = 0
descuento = 0
totalPagar = 0

menu_Chinos = True

while menu_Chinos:
    os.system("cls")
    print("Shin Whe Wensha")
    print("1. Camaron Mandarin \t $11000")
    print("2. Carne Mongoliana \t $10000")
    print("3. Chapsui Pollo \t $9500")
    print("4. Chapsui Carne \t $12000")
    print("5. Parrillada China \t $15000")
    print("6. Pagar")
    print("7. Cancelar Pedido")
    opcion_menu = 0
    try:
        opcion_menu = int(input("Ingrese su opción > "))
    except:
        print("Se esperaba un numero")
        time.sleep(2)
        os.system("cls")

    if opcion_menu < 1 or opcion_menu > 7:
        print("La opcion ingresada no es valida")
        time.sleep(1)
        os.system("cls")
    else:
        if opcion_menu == 1:
            try:
                cantidad_camaronMandarin = int(input("Ingrese la cantidad de camaron mandarin que desea comprar > "))
            except:
                print("Se esperaba un numero")
                time.sleep(2)
                os.system("cls")
        elif opcion_menu == 2:
            try:
                cantidad_carneMongoliana = int(input("Ingrese la cantidad de carne mongoliana que desea comprar > "))
            except:
                print("Se esperaba un numero")
                time.sleep(2)
                os.system("cls")
        elif opcion_menu == 3:
            try:
                cantidad_chapsuiPollo = int(input("Ingrese la cantidad de chapsui pollo que desea comprar > "))
            except:
                print("Se esperaba un numero")
                time.sleep(2)
                os.system("cls")
        elif opcion_menu == 4:
            try:
                cantidad_chapsuiCarne = int(input("Ingrese la cantidad de chapsui carne que desea comprar > "))
            except:
                print("Se esperaba un numero")
                time.sleep(2)
                os.system("cls")
        elif opcion_menu == 5:
            try:
                cantidad_parrilladaChina = int(input("Ingrese la cantidad de parrillada china que desea comprar > "))
            except:
                print("Se esperaba un numero")
                time.sleep(2)
                os.system("cls")
        elif opcion_menu == 6:
            if cantidad_camaronMandarin == 0 and cantidad_carneMongoliana == 0 and cantidad_chapsuiCarne == 0 and cantidad_chapsuiPollo == 0 and cantidad_parrilladaChina == 0:
                print("No se ha ingresado ningun platillo")
                time.sleep(2)
                os.system("cls")
            else:
                os.system("cls")
                menu_descuento = True
                while menu_descuento: 
                    print("=== Tipo de Cliente ===")
                    print("1. Cliente Frecuente \t\t 15% ")
                    print("2. Tarjeta Vecino \t\t 10%")
                    print("3. Carnet Tercera Edad \t\t 7%")
                    print("4. No Aplica Descuento")
                    opcion_descuento = 0
                    try:
                        opcion_descuento = int(input("Ingrese su opción > "))
                    except:
                        print("Se esperaba un numero")
                        time.sleep(2)
                        os.system("cls")
                    
                    if opcion_descuento < 1 or opcion_descuento > 4:
                        print("La opción ingresada no es valida. Intente nuevamente")
                        time.sleep(2)
                        os.system("cls")
                    else:
                        #validar los descuentos
                        if opcion_descuento == 1:
                            descuento = 15
                        elif opcion_descuento == 2:
                            descuento = 10
                        elif opcion_descuento == 3:
                            descuento = 7
                        elif opcion_descuento == 4:
                            descuento = 0
                        else:
                            print("Opcion No Disponible")
                            time.sleep(2)
                            os.system("cls")
                        menu_descuento = False
                #boleta
                os.system("cls")
                print("                                      Shin Whe Wensha")
                print("=========================================================")
                print(f"Total De Productos: {cantidad_camaronMandarin + cantidad_carneMongoliana + cantidad_chapsuiPollo + cantidad_chapsuiCarne+cantidad_chapsuiPollo+cantidad_parrilladaChina}")
                print("=========================================================")
                if cantidad_camaronMandarin > 0:
                    print(f"Cantidad de Camaron Mandarin: {cantidad_camaronMandarin} \t $ {cantidad_camaronMandarin * 11000}")
                if cantidad_carneMongoliana > 0:
                    print(f"Cantidad de Carne Mongoliana: {cantidad_carneMongoliana} \t $ {cantidad_carneMongoliana * 10000}")
                if cantidad_chapsuiPollo > 0:
                    print(f"Cantidad de Chapsui Pollo: {cantidad_chapsuiPollo} \t\t $ {cantidad_chapsuiPollo * 9500}")
                if cantidad_chapsuiCarne > 0:
                    print(f"Cantidad de Chapsui Carne: {cantidad_chapsuiCarne} \t\t $ {cantidad_chapsuiCarne * 12000}")
                if cantidad_parrilladaChina > 0:
                    print(f"Cantidad de Parrillada China: {cantidad_parrilladaChina} \t $ {cantidad_parrilladaChina * 15000}")
                print("=========================================================")
                subtotal = cantidad_camaronMandarin * 11000 + cantidad_carneMongoliana * 10000 + cantidad_chapsuiPollo * 9500 + cantidad_chapsuiCarne * 12000 + cantidad_parrilladaChina * 15000
                print(f"subtotal: $ {subtotal}")
                print(f"Descuento: {descuento}% \t ${subtotal * descuento/100}")
                totalPagar = subtotal - (subtotal * descuento/100)
                print(f"Total a pagar: $ {totalPagar}")
                print("=========================================================")
                print("=== Gracias Por Su Compra ===")
                menu_Chinos = False

        elif opcion_menu == 7:
            if cantidad_camaronMandarin == 0 and cantidad_carneMongoliana == 0 and cantidad_chapsuiCarne == 0 and cantidad_chapsuiPollo == 0 and cantidad_parrilladaChina == 0:
                print("No se ha ingresado ningun platillo")
                time.sleep(2)
                os.system("cls")
            else:    
                try:
                    confirmar = int(input("¿De verdad deseas cancelar el pedido? 1.Si / 2.no > "))

                    while confirmar < 1 or confirmar > 2:
                        print("La opción ingresada no es valida. Intente nuevamente")
                        time.sleep(2)
                        os.system("cls")
                        confirmar = int(input("¿De verdad deseas cancelar el pedido? 1.Si / 2.no > "))

                    if confirmar == 1:
                            print("=== Pedido Cancelado Por El Usuario ===")
                            time.sleep(2)
                            os.system("cls")
                            menu_Chinos = False
                    else:
                        opcion_menu = 6
                except:
                    print("Se esperaba un numero")
                    time.sleep(2)
                    os.system("cls")
                else:
                    opcion_menu = 6
        else:
            print("Opcion No Disponible")
            time.sleep(2)
            os.system("cls")
