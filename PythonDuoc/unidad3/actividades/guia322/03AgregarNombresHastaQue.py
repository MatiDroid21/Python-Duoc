import os

confirmacion = "si"
nombres = []
nom = ""
os.system("cls")
while confirmacion == "si":
    nom = input("Ingrese un nombre >> ")
    nombres.append(nom)
    print(nombres)

    confirmacion = input("¿Deseas Agregar Otro Registro si/no? >> ").lower()

    if confirmacion == "si".lower():
        os.system("cls")
    elif confirmacion == "no".lower():
        nombres.sort()
        nombres.remove(nombres[0])        
        break
    else:
        print("La opción ingresada no es valida. Intente nuevamente")
        time.sleep(1)
        confirmacion = input("¿Deseas Agregar Otro Registro si/no? >> ").lower()
        
        
    
print(nombres)
