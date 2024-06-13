import os
import time

# cine
def menu_general():
    os.system("cls")
    print("== MENU ==")
    print("1. Mostrar Sala")
    print("2. Comprar Entrada")
    print("3. Eliminar Entrada")
    print("4. Mostrar Ventas")
    print("5. Salir")

def elegir_opcion(max_opciones):
    while True:
        opcion = 0
        try:
            opcion = int(input("Seleccione una de las opciones disponibles >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opciones:
            print("Opción no válida \n")
        else:
            return opcion

sala = [
    ['A1','A2','A3','A4','A5'],
    ['B1','B2','B3','B4','B5'],
    ['C1','C2','C3','C4','C5'],
    ['D1','D2','D3','D4','D5'],
    ['E1','E2','E3','E4','E5'],
]

todas_las_entradas = []
entradas_ocupadas = []
registro_cliente = []

def imprimir_sala():
    
    print("\n== SALA 7 ==\n")
    print(f"Clientes : {registro_cliente}")
    print(f"ENTRADAS OCUPADAS : {entradas_ocupadas}")

    imprimir = ""

    for fila in sala:
        for asiento in fila:
            todas_las_entradas.append(asiento) # acá dejamos dentro del array todas las entradas
            if asiento in entradas_ocupadas:
              imprimir += f"| {colorRojo(asiento)} "
              #imprimir += f"|{asiento} "
            else:
              imprimir += f"| {colorVerde(asiento)} "
        imprimir += "|\n"    
    print(f"Asientos Ocupados : {entradas_ocupadas}")
    print(imprimir)
    print("\n")

def comprar_entrada():
    entrada = input("Selecciona una de las entradas disponibles >> ").upper()

    if entrada in todas_las_entradas and entrada not in entradas_ocupadas:
        print("ENTRADA ESTA DISPONIBLE")
        entradas_ocupadas.append(entrada)
        registrar(entrada)
    else:
        print("No es un asiento válido ")

def registrar(entrada):
    nombre = input("Ingresa un nombre >> ")
    apellido = input("Ingresa un apellido >> ")
    edad = int(input("Ingrese su edad >> "))
    registro_cliente.append([entrada,nombre,apellido,edad])

def colorVerde(texto):
    return f"\033[2:32m{texto}\033[0m"#verde

def colorRojo(texto):
    return f"\033[2:31m{texto}\033[0m" #rojo

def mostrarVentas():
    ventas = "\n ==== Ventas ===="
    ventas += "|  Asiento  | Nombre \t| Apellido \t| Edad |\n"
    for cliente in registro_cliente:
        print(cliente)
        for info in cliente:
            ventas += f"| {info} \t"

salir = False
while not salir:
    menu_general()
    opcion = elegir_opcion(5)

    if opcion == 1:
        print("== SALA ==")
        imprimir_sala()

    elif opcion == 2:
        print("== Comprar entrada ==")
        imprimir_sala()
        comprar_entrada()

    elif opcion == 3:
        print("== Eliminar entrada ==")
    elif opcion == 4:
        print("== Mostrar Ventas ==")
        mostrarVentas()
    elif opcion == 5:
        print("== SALIR ==")
        os.system("cls")
        print("Cerrando procesos.")
        time.sleep(1)
        os.system("cls")
        print("Cerrando procesos..")
        time.sleep(1)
        os.system("cls")
        print("Cerrando procesos...")
        time.sleep(3)
        os.system("cls")
        print("Ejecución Finalizada")
        salir = True
    else:
        print("Opción no disponible")

    input("Presione enter para continuar")