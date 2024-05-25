import os

os.system("cls")

nombres = []
apellidos = []

for nom in range(3):
    print(f"Se registra el nombre n° {nom+1}")
    name = input("Ingrese un nombre >>> ")
    nombres.append(name)

for ape in range(3):
    print(f"Se registra el apellido n° {ape+1}")
    lastname = input("Ingrese un apellido >>> ")
    apellidos.append(lastname)

os.system("cls")

personas = [nombres,apellidos]
nombres.sort()
apellidos.sort()

print(nombres)
print(apellidos)

