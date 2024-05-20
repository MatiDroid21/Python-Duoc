import os
import time

os.system("cls")
nombre = ""
paterno = ""
materno = ""

while nombre == "":
    try:
        nombre = input("Ingresa tu nombre >> ")
        if nombre == "":
            print("Tienes que ingresar un nombre")
            time.sleep(1)
            os.system("cls")
    except:
        print("Error en el ingreso de datos")
        time.sleep(1)
        os.system("cls")

while paterno == "":
    try:
        paterno = input("Ingresa tu apellido paterno >> ")
        if paterno == "":
            print("Tienes que ingresar un apellido paterno")
            time.sleep(1)
            os.system("cls")
    except:
        print("Error en el ingreso de datos")
        time.sleep(1)
        os.system("cls")


while materno == "":
    try:
        materno = input("Ingresa tu apellido materno >> ")
        if materno == "":
            print("Tienes que ingresar un apellido materno")
            time.sleep(1)
            os.system("cls")
    except:
        print("Error en el ingreso de datos")
        time.sleep(1)
        os.system("cls")

primeraparte = nombre[:2].upper()
segundaparte = paterno[3:].lower()
terceraparte = len(materno)

print(f"La contraseña generada para el usuario es: {primeraparte}{segundaparte}{terceraparte}")
