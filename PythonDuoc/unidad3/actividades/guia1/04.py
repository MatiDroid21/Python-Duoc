import os
os.system("cls")
todos_los_usuarios = []
todas_las_claves = []
nombre = ""
clave = ""

def menu():
    print("=== Menu ===")
    print("1. Iniciar Sesion")
    print("2. Registrarse")
    print("3. Borrar Cuenta")
    print("4. Salir Del Sistema")

def elegir_opcion(max_opcion):
    opcion = 0
    try:
        opcion = int(input("Ingrese una de las opciones disponibles >> "))
    except:
        print("Se esperaba un numero")

    if opcion <= 0 or opcion > max_opcion:
        print("Debes escoger una de las opciones disponibles. ")
    else:
        return opcion

def crear_usuario():
    nombre = input("Ingrese el nombre de usuario >> ")
    clave = input("Ingrese la clave para su usuario >> ")

    if nombre in todos_los_usuarios:
        print("Ese usuario se encuentra ya registrado.")
    else:
        todos_los_usuarios.append(nombre)
        todas_las_claves.append(clave)
        print(f"{nombre} Has sido registrado correctamente.")

        
def eliminar_cuenta():
    nombre = input("Ingresa tu nombre de usuario")
    if nombre in todos_los_usuarios:
        todos_los_usuarios.pop(nombre)
        todas_las_claves.pop(nombre)
        print("Su cuenta ha sido eliminada de nuestros servicios")
    else:
        print("El usuario no existe.")

def login(nombre, clave):
    nombre = input("Ingrese su nombre de usuario >> ")
    clave = input("Ingrese su clave de acceso >> ")

    if nombre in todos_los_usuarios:
        index = todos_los_usuarios.index(nombre)
        if todas_las_claves[index] == clave:
            print(f"Bienvenido {nombre}")
        else:
            print("Credenciales incorrectas")
    else:
        print("Usuario no existe en sistema")


salir = False
menu()
opcion = elegir_opcion(5)

while not salir:
    if opcion == 1:
        login(nombre,clave)

    elif opcion == 2:
        crear_usuario()
    elif opcion == 3:
        eliminar_cuenta()
    elif opcion == 4:
        print("Hasta pronto !")
        salir = True
    else:
        print("Se ha ingresado una opcion no valida")