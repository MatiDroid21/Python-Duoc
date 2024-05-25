import os 
os.system("cls")

# try: #inicializa la captura de errores.
#     numero = int(input("Ingrese numero > "))
#     print(f"El numero ingresado es {numero}")
# except:#esto se ejecuta si ocurre un error.
#     print("Error, se esperaba un numero")


#formas de hacer while.
while True:
    print("El ciclo sin fin.")
    break

#break rompe la ejecucion del codigo.

#forma2
ciclo = True
while ciclo:
    print("Ciclo sin fin en otro bucle")
    print("Ciclo sin fin en otro bucle")
    print("Ciclo sin fin en otro bucle")
    print("Ciclo sin fin en otro bucle")
    ciclo = False
    
#forma3
numero = 1
while numero < 10:
    numero +=1
    print(f"numero = {numero}")
    