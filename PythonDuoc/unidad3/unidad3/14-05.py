import os 
import time

## registros de personas con arreglos
os.system("cls")
listado_notas = []

print(f"listado notas inicial {listado_notas}")
    
for i in range(4):
    nota = float(input(f"Ingrese nota {i+1} >>> "))
    listado_notas.append(nota)
        
listado_notas.sort()
print(f"listado notas final {listado_notas}")


 