import os
import time
os.system("cls")

nombres = [] #array vacio que luego llenaremos con nombres
nombre = ""

for i in range(3):
    try:
        nombre = input("Ingrese un nombre >> ")
        if nombre == "":
            print("No se ingreso un nombre o ingresaste algo nada que ver")
            print(nombres)
            try:
                nombre = input("Ingrese un nombre >> ")
                nombres.remove(nombres[0])
            except:
                print("Ingresa algo pkipfjpo")
        else:
            nombres.append(nombre)
            print(f"Nombres en el listado: {nombres}")
    except ValueError:
        print("No se ingreso un nombre o ingresaste algo nada que ver")

os.system("cls")

print("validando...")

os.system("cls")
print("Espere un momento...")
time.sleep(1)

print(f"El nombre más largo es: {nombres[-1]} con cantidad de caracteres {len(nombres[-1])}")
