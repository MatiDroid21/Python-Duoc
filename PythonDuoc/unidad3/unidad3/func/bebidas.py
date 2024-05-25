import os
import time
os.system("cls")

def menu():
    print("=== Bebida ===")
    print("1. Coca-Cola")
    print("2. Pepsi")   
    print("3. Fanta")
    
   # opcion = int(input("Ingrese una de las opciones disponibles"))
    opcion = 0
    while opcion < 1 or opcion > 3:
        try:
            opcion = int(input("Ingrese una de las opciones disponibles >> "))
            if opcion <1 or opcion > 3:
                print("La opción ingresada no es valida. Intente nuevamente")
                time.sleep(1)
               # os.system("cls")
            else:
                Seleccionbebidas(opcion)
        except:
            print("Error: Se esperaba un numero. Por favor eliga una de las opciones disponibles")

def Seleccionbebidas(op):
    if op == 1:
        cantidad = 0
        print("Usted seleccionó Coca-Cola")
        cantidad = int(input("Ingrese cantidad de bebidas a comprar >> "))
        
        boleta("Coca-Cola", cantidad)
    elif op == 2:
        cantidad = 0
        print("Usted seleccionó Pepsi")
        cantidad = int(input("Ingrese cantidad de bebidas a comprar >> "))
        boleta("Pepsi",cantidad)
    elif op == 3:
        cantidad = 0
        print("Usted seleccionó Fanta")
        cantidad = int(input("Ingrese cantidad de bebidas a comprar >> "))
        boleta("Fanta",cantidad)
    else:
        print("La opción ingresada no es valida. Intente nuevamente")
        time.sleep(1)
        os.system("cls")

def boleta(bebida, cantidad):
    os.system("cls")
    print("=== Boleta De Las Bebidas ===")
    print(f"Bebida Seleccionada: {cantidad}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio: {1000 * cantidad}")


menu()
