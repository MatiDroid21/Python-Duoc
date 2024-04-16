import os
os.system("cls")

print("Hello World!!")
saludo = "Hello World"

print("desde variable",saludo)

#######################3

"""
comentar en varias lineas
"""

# Cómo consultar el tipo de dato
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
print(type(print("Mi cadena de texto")))  # Tipo 'NoneType'


# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))

print("Hola " + "Python " + "¿Qué tal?") ## concatenar una forma
print("Hola","Python","¿Qué tal?") # concatenar forma dos.