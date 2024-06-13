import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

todas_las_compras = []
todosListados = []

os.system("cls")

def menu_general():
    os.system("cls")
    print("=== Gasxplosive ===")
    print(f"{Fore.GREEN}1. Registrar Pedido{Style.RESET_ALL}")
    print(f"{Fore.BLUE}2. Listar Pedidos{Style.RESET_ALL}")
    print(f"{Fore.RED}3. Imprimir Hoja De Ruta{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}4. Finalizar Programa{Style.RESET_ALL}")

def validar_opciones(max_opcion):
    while True:
        opcion = 0
        try:
            opcion = int(input("Ingrese una de las opciones disponibles >> "))
        except:
            pass

        if opcion < 1 or opcion > max_opcion:
            input("Opcion no disponible. Presione Enter Para Continuar") 
        else:
            return opcion
        
def registar_pedido():
    os.system("cls")
    print("=== Registrar Pedido ===")
    nombre = input("Ingrese nombre de cliente >> ")
    apellido = input("Ingrese apellido de cliente >> ")
    direccion = input("Ingrese direccion domicilio >> ")
    comuna = input("Ingrese comuna >> ")
    cilindros = comprar_cilindros()

    compra = ([nombre,apellido,comuna,direccion,cilindros])
    todas_las_compras.append(compra)
    input(todas_las_compras)

def comprar_cilindros():
    cantidad_5kg = 0
    cantidad_15kg = 0
    cantidad_45kg = 0

    while True:
        os.system("cls")
        print("=== Comprar Cilindros ===")
        print("1. 5KG")
        print("2. 15KG")
        print("3. 45KG")
        print("Ingrese una de las opciones")
        opcion = validar_opciones(3)
        if opcion == 1:
            cantidad_5kg += int(input("Ingrese la cantidad de cilindros de 5KG a comprar "))
        elif opcion == 2:
            cantidad_15kg += int(input("Ingrese la cantidad de cilindros de 15KG a comprar "))
        elif opcion == 3:
           cantidad_45kg += int(input("Ingrese la cantidad de cilindros de 45KG a comprar "))

        print("Desea seguir comprando? 1.si / 2.no")
        salir = validar_opciones(2)
        if salir == 2:
            return {
                "5KG":cantidad_5kg,
                "15KG":cantidad_15kg,
                "45": cantidad_45kg,
            }

def mostrarCompras():
    if len(todas_las_compras) <= 0:
        print("No hubo compras de gas")
    else:
        print("Ventas")
        print(todas_las_compras)



def iniciarPrograma():
    while True:
        menu_general()
        opcion = validar_opciones(4)

        if opcion == 1:
            print(f"{Fore.GREEN}Registrar Pedido{Style.RESET_ALL}")
            registar_pedido()

        elif opcion == 2:
            print(f"{Fore.BLUE}Listar Pedidos{Style.RESET_ALL}")
            mostrarCompras()
        elif opcion == 3:
            print(f"{Fore.RED}Imprimir Hoja De Ruta{Style.RESET_ALL}")
        elif opcion == 4:
            print(f"{Fore.MAGENTA}Finalizando Programa...{Style.RESET_ALL}")
            return
        
        input()

iniciarPrograma()
        
