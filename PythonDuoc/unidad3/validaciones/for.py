import os 
os.system("cls")

#for basico, repite x cantidad de veces
for i in range(10):
    print(f"Hola {i} veces")
print("===========================")

#for con valor de inicio y valor final.
for c in range(5,10):
    print(f"ciclo {c}")
print("============================")

#for con salto 
for i in range(2,10,2): #el tercer parametro es cuanto aumenta i en cada ciclo.
    print(f"ciclo {i}, salto de 2 en 2, eso es el ultimo numero del for")

    