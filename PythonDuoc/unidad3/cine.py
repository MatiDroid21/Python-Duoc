import os
import time

os.system("cls")

cine = [
    ['A1','A2','A3','A4'],
    ['B1','B2','B3','B4'],
    ['C1','C2','C3','C4'],
    ['D1','D2','D3','D4']
]

todosLosAsientos = []
asientos_comprados = [] #la primera vez no tiene nada


#aux
auxAsientos = "=== CINE ===\n"

for fila in cine:
    for asiento in fila:
        auxAsientos += f"|{asiento}|"
        todosLosAsientos.append(asiento)
    auxAsientos += "\n"
    
print(auxAsientos)
asiento_a_comprar = input("Selecciona uno de los asientos disponibles > ")

if asiento_a_comprar in todosLosAsientos:
    print(f"Asiento elegido: {asiento_a_comprar}")
else:
    print("Asiento no existe")
