import os
os.system("cls")

nombre = "Matias Chavez".lower()
## como obtener la cantidad total de vocales y consonantes?
vocal = 0
consonante = 0

for letra in nombre:
    if letra in 'aeiou': ##si la letra se encuentran dentro de a-e-i-o-u que sume
        vocal += 1 #pregunta si hay letras en el nombre. De encontrarlas que le sume 1 a vocales
    elif letra == " ": 
        pass 
    else:
        consonante += 1

print(f"La cantidad de vocales es: {vocal}")
print(f"La cantidad de consonantes es: {consonante}")
