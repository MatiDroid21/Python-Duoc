import os
os.system("cls")

edad = int(input("Ingrese edad > "))

if edad == 0:
  print("Nacio")
elif edad > 0 and edad <= 5:
    print("Es un niño/niña")
elif edad > 5 and edad < 18:
    print("Es un joven")
elif edad >= 18 and edad <= 64:
    print("Es adulto")
elif edad >= 65:
    print("Es abuelito")
else:
    print("no se, tal vez se murio o se esta crafteando XD")

print("Fin de la ejecucion")