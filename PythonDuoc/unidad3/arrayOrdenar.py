import os
import time
os.system("cls")

notas = []
cantNotas = 0

while cantNotas <= 1:
    try:
        cantNotas = int(input("Ingrese la cantidad de notas del estudiante >> "))
    except:
        print("Debe ser numero")
        time.sleep(1)

for i in range(cantNotas):
    try:
        nueva_nota = float(input("Ingrese nota >> "))
    except:
        print("Debe ser decimal. PORQUE SI XD")
        time.sleep(1)

    notas.append(nueva_nota)
    notas.sort()
    print(f"Las notas del estudiante son {notas}")

nombre = "Alan Brito"
print(len(nombre))