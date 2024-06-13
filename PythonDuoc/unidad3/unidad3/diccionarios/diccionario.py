import os
import time
os.system("cls")

persona = {
    "nombre":"Mati",
    "apellido":"Droid",
    "edad":21,
    "genero":"M",
    "telefonos":[96786789,9567659,7897998],
    "soltero":True
}

print(persona) #accede a todo el diccionario
print(persona["edad"]) #accede a un campo especifico
time.sleep(1)
persona["edad"] = 20 #cambiamos el valor de un campo en especifico.

print(persona["edad"])

os.system("cls")

#agregar elementos al diccionario
persona["trabajo"] = "soporte"

for key in persona:
    print(f"clave: {key} / valor: {persona[key]}") #asi puedes recorrer un diccionario.




