import os
os.system("cls")

#menu simple
print("=== BEBIDAS ENERGETICAS ===")
print("1. Monster")
print("2. Red Bull")
print("3. Score")

opcion = int(input("Ingrese una de las opciones > "))

#validar rango
while opcion <1 or opcion > 3:
    print("Opcion invalida, ingrese una de las opciones disponibles.")
    opcion = int(input("Ingrese una de las opciones > "))
if opcion < 1 or opcion > 3:
    print("Opcion invalida, ingrese una de las opciones disponibles.")
elif opcion == 1:
    print("Seleccionaste Monster")
elif opcion == 2:
    print("Seleccionaste Red Bull")
elif opcion == 3:
    print("Seleccionaste Score")

