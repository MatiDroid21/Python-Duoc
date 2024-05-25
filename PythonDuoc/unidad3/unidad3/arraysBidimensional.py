import os
os.system("cls")

doctores =[ 
    ["Pedro","Pascal","Urgencias"],
    ["Maria","Dolores","Enfermeria"],
    ["Alan","Brito","Auxiliar"]
]

print(doctores[2][2]) #!imprime Enfermeria

for doctor in doctores:
    for info in doctor:
        print(info) #muestra el array del doctor

for doctor in doctores:
    print(doctor[2])


