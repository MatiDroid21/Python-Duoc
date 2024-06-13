#pip install colorama 
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()

def menu_general():
    os.system("cls")
    print("==== MENU ====")
    print(f"{Fore.GREEN}1. Mostrar Sala{Style.RESET_ALL}")
    print(f"{Fore.BLUE}2. Comprar Entrada{Style.RESET_ALL}")
    print(f"{Fore.RED}3. Eliminar Entrada{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}4. Mostrar Ventas{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}5. Salir{Style.RESET_ALL}")

def elegir_opcion(max_opciones):
    while True:
        opcion = 0
        try:
            opcion = int(input("Seleccione una de las opciones disponibles >> ").upper())
        except ValueError:
            pass #igual ver si podemos mandar un error.
        if opcion < 1 or opcion > max_opciones:
            print("Opción no válida o Opción  \n")
        else:
            return opcion



sala = [
    ['A1', 'A2', 'A3', 'A4', 'A5'],
    ['B1', 'B2', 'B3', 'B4', 'B5'],
    ['C1', 'C2', 'C3', 'C4', 'C5'],
    ['D1', 'D2', 'D3', 'D4', 'D5'],
    ['E1', 'E2', 'E3', 'E4', 'E5'],
]

todas_las_entradas = []
entradas_ocupadas = []

def imprimir_sala():
    print("\n== SALA 7 ==\n")
   
    print(f"ENTRADAS OCUPADAS: {entradas_ocupadas}\n")

    for fila in sala:
        for asiento in fila:
            todas_las_entradas.append(asiento) # ?
            if asiento in entradas_ocupadas:
                imprimir = f"{Back.RED}{Fore.WHITE}{asiento}{Style.RESET_ALL}"
            else:
                imprimir = f"{Back.GREEN}{Fore.BLACK}{asiento}{Style.RESET_ALL}"
            print(f"| {imprimir} ", end="")
        print("|")

def comprar_entrada():
    if entradas_ocupadas.count == 25:
        print("Sala Llena")
    else:
        entrada = input("Selecciona una de las entradas disponibles >> ")
        if entrada in todas_las_entradas and entrada not in entradas_ocupadas:
            print("ENTRADA ESTÁ DISPONIBLE")
            entradas_ocupadas.append(entrada)
        else:
            print("No es un asiento válido o ya está ocupado.")

def eliminar_entrada():
    print(entradas_ocupadas)
    entrada = input("Selecciona una de las entradas a eliminar >> ")
    if entrada in entradas_ocupadas: #recorrer las entradas ocupadas.
        #print("ENTRADA LIBERADA")
        print(f"Asiento {entrada} liberado")
        entradas_ocupadas.remove(entrada)
    elif len(entradas_ocupadas) == 0:
        print("Sala Vacia")
    else:
        print(f"Asiento {entrada}, no se encontraba ocupado.")
        
 
def mostrar_ventas():
    if len(entradas_ocupadas) <= 0:
        print("No hubo venta de entradas")
    else:
        print("\n== VENTAS ==")
        precio_ticket = 2000
        venta_total = precio_ticket * len(entradas_ocupadas)
        print(f"Entradas ocupadas: {entradas_ocupadas}")
        print(f"Número de entradas vendidas: {len(entradas_ocupadas)}")
        print(f"Dinero Recaudado: {venta_total}")

salir = False
while not salir:
    menu_general()
    opcion = elegir_opcion(5)

    if opcion == 1:
        imprimir_sala()
    elif opcion == 2:
        imprimir_sala()
        comprar_entrada()
    elif opcion == 3:
        imprimir_sala()
        eliminar_entrada()
    elif opcion == 4:
        mostrar_ventas()
    elif opcion == 5:
        os.system("cls")
        print("== SALIR ==")
        print("Programa Finalizado")
        salir = True
    else:
        print("Opción no disponible")

    input("Presiona Enter para continuar...")
