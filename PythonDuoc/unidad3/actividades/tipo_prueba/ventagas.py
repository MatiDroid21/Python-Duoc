import os
import colorama
from colorama import Fore, Style
# print(f"{Fore.GREEN}1. Registrar Pedido{Style.RESET_ALL}") ! para recordar

os.system("cls")

todas_las_compras = []

def menu_general():
    os.system("cls")
    print("=== GAS ===")
    print(f"{Fore.GREEN}1. Registrar Pedido {Style.RESET_ALL}")
    print(f"{Fore.BLUE}2. Listar todos los pedidos {Style.RESET_ALL}")
    print(f"{Fore.RED}3. Imprimir hoja de ruta {Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}4. Salir del sistema {Style.RESET_ALL}")

def validar_opciones(max_option):
    while True:
        opcion = 0
        try:
            opcion = int(input("Ingrese una de las opciones disponibles >> "))
        except:
            pass

        if opcion < 1 or opcion > max_option:
            input("la opción no disponible, presione enter para continuar >> ")
        else:
            return opcion

def registrar_pedido():
    os.system("cls")
    print("=== REGISTRAR PEDIDO ===")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    comuna = input("Ingrese su comuna: ")
    direccion = input("Ingrese direccion domicilio: ")
    sector = input("Ingrese su sector: ")
    cilindros = comprar_cilindros()

    todas_las_compras.append([nombre, apellido, comuna, direccion, sector, cilindros])

    #input(todas_las_compras)


def comprar_cilindros():
    cant_5kg = 0
    cant_15kg = 0
    cant_45kg = 0

    while True:
        os.system("cls")
        print("== COMPRAR CILINDROS ==")
        print("1. 5kg")
        print("2. 15kg")
        print("3. 45kg")
        opcion = validar_opciones(3)

        if opcion == 1:
            cant_5kg += int(input("Ingrese la cantidad de cilindros de 5Kg que desea >> "))
        elif opcion == 2:
            cant_15kg += int(input("Ingrese la cantidad de cilindros de 15Kg que desea >> "))
        elif opcion == 3:
            cant_45kg += int(input("Ingrese la cantidad de cilindros de 45Kg que desea >> "))
        
        print("Desea seguir comprando | 1:Si 2:NO | >> ")
        salir = validar_opciones(2)

        if salir == 2:
            return { 
                "5kg": cant_5kg,
                "15kg": cant_15kg,
                "45kg": cant_45kg
            }

def listar_pedidos():
    os.system("cls")
    print(todas_las_compras)


def iniciar_programa():
    while True:
        menu_general()
        opcion = validar_opciones(4)

        if opcion == 1:
            registrar_pedido()
        elif opcion == 2:
            print("| CLIENTE \t\t| COMUNA \t\t| DIRECCION \t\t| SECTOR \t\t| 5KG \t\t| 15KG \t\t| 45KG \t\t|")
            for compras in todas_las_compras:
                #[['ewe', 'ewe', '3}', {'5kg': 0, '15kg': 33, '45kg': 1111111111111111111111111111111111111111111111111111111}]]
                print(f"| {compras[0]} {compras[1]} \t\t| {compras[2]} \t\t| {compras[3]} \t\t| {compras[4]} \t\t|{compras[5]['5kg']} \t\t| {compras[5]['15kg']} \t\t| {compras[5]['45kg']} \t\t|")

        elif opcion == 3:
            print("3. Imprimir hoja de ruta")
        elif opcion == 4:
            print("Saliendo del sistema, xiiao")
            return
        
        input()

iniciar_programa()