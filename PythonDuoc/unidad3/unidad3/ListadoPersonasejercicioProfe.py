## registro de personas

import os
import time

persona = []

nombre = input("Ingrese su nombre >>> ")
apellido = input("Ingrese su apellido >>> ")
edad = int(input("Ingrese su edad >>> "))
peso = float(input("Ingrese su peso >>> "))
estatura = float(input("Ingrese su estatura >>> "))

persona.append(nombre)
persona.append(apellido)
persona.append(edad)
persona.append(peso)
persona.append(estatura)

print(persona)
print(persona[:2]) #los primeros 2 elementos
print(persona[-2:]) # los ultimos elementos