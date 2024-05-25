import os
import time #libreria para esperar x tiempo
os.system("cls")

#preguntar al usuario cuantos pasajes va a vender
menu = True
suma_pasaje = 0 
precio_pasaje = 0

while menu:
    try:
        precio_pasaje = int(input("Ingrese precio de pasaje: "))
        cantPasajes = int(input("Ingrese la cantidad de pasajes a vender: "))
        #print(cantPasajes)
        menu = False
    except:
        print("Se esperaba un numero")
        time.sleep(1)
        os.system("cls")

for i in range(cantPasajes):
    i+=1
    suma_pasaje = precio_pasaje * i
  #estoy testeando ndjhwhbjdwinh nhfxliexngxi
   
print(f"El total a pagar es {suma_pasaje}")


