import os 
os.system("cls")

try: #inicializa la captura de errores.
    numero = int(input("Ingrese numero > "))
    print(f"El numero ingresado es {numero}")
except:#esto se ejecuta si ocurre un error.
    print("Error, se esperaba un numero")

    
