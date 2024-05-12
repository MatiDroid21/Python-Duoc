import os
os.system("cls")

pokemones = []

for i in range(5):
    nuevo_pokemon = input("Ingrese un pokemon >> ")
    #para agregar elementos al array se usa .append()
    pokemones.append(nuevo_pokemon)

    print(f"Pokemones en el listado: {pokemones}")
