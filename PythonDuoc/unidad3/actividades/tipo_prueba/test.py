import os
import colorama
from colorama import Fore, Style

colorama.init()

todas_las_compras = []

def menu_general():
    os.system("cls")
    print("=== Gasxplosive ===")
    print(f"{Fore.GREEN}1. Registrar Pedido{Style.RESET_ALL}")
    print(f"{Fore.BLUE}2. Listar Pedidos{Style.RESET_ALL}")
    print(f"{Fore.RED}3. Imprimir Hoja De Ruta{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}4. Finalizar Programa{Style.RESET_ALL}")

def validar_opciones(max_opcion):
    while True:
        try:
            opcion = int(input("Ingrese una de las opciones disponibles >> "))
            if 1 <= opcion <= max_opcion:
                return opcion
        except ValueError:
            pass
        input("Opción no disponible. Presione Enter Para Continuar")

def registrar_pedido():
    os.system("cls")
    print("=== Registrar Pedido ===")
    nombre = input("Ingrese nombre del cliente >> ")
    apellido = input("Ingrese apellido del cliente >> ")
    direccion = input("Ingrese dirección del cliente >> ")
    comuna = input("Ingrese comuna >> ")
    cilindros = comprar_cilindros()

    compra = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Comuna": comuna,
        "Dirección": direccion,
        "Cilindros": cilindros
    }
    todas_las_compras.append(compra)
    input("Pedido registrado exitosamente. Presione Enter para continuar.")

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
        opcion = validar_opciones(3)
        if opcion == 1:
            cantidad_5kg += int(input("Ingrese la cantidad de cilindros de 5KG a comprar >> "))
        elif opcion == 2:
            cantidad_15kg += int(input("Ingrese la cantidad de cilindros de 15KG a comprar >> "))
        elif opcion == 3:
            cantidad_45kg += int(input("Ingrese la cantidad de cilindros de 45KG a comprar >> "))

        print("¿Desea seguir comprando? 1. Sí / 2. No")
        salir = validar_opciones(2)
        if salir == 2:
            return {
                "5KG": cantidad_5kg,
                "15KG": cantidad_15kg,
                "45KG": cantidad_45kg
            }

def mostrar_compras():
    os.system("cls")
    if len(todas_las_compras) == 0:
        print("No hubo compras de gas")
    else:
        print("=== Ventas ===")
        for compra in todas_las_compras:
            print(compra)
    input("Presione Enter para continuar.")

def imprimir_hoja_de_ruta():
    os.system("cls")
    print("=== Imprimir Hoja De Ruta ===")
    print("Seleccione un sector (Centro, Colina, Industrias)")
    sector = input("Ingrese el sector >> ").strip().capitalize()
    
    ruta_pedidos = [compra for compra in todas_las_compras if compra["Comuna"].lower() == sector.lower()]

    if not ruta_pedidos:
        print(f"No hay pedidos para el sector {sector}.")
        input("Presione Enter para continuar.")
        return

    nombre_archivo = f"hoja_de_ruta_{sector}.txt"
    with open(nombre_archivo, "w") as file:
        for pedido in ruta_pedidos:
            file.write(str(pedido) + "\n")
    
    print(f"Hoja de ruta generada en el archivo {nombre_archivo}.")
    input("Presione Enter para continuar.")

def iniciar_programa():
    while True:
        menu_general()
        opcion = validar_opciones(4)

        if opcion == 1:
            registrar_pedido()
        elif opcion == 2:
            mostrar_compras()
        elif opcion == 3:
            imprimir_hoja_de_ruta()
        elif opcion == 4:
            print(f"{Fore.MAGENTA}Finalizando Programa...{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    iniciar_programa()
