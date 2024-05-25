import os

os.system("cls")


def menuCalculadora():
    print("=== Calculadora ===")
    print("1. Suma")
    print("2. Resta")
    opcion = int(input("Ingrese una opcion >> "))
    calculadora(opcion)
    

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    result = num1 - num2
    print(f"El resultado de la resta es {result}")

def calculadora(op):
    if op == 1:
        n1 = int(input("Ingresa el primer numero >> "))
        n2 = int(input("Ingresa el segundo numero >>> "))
        suma(n1,n2) 
        print(f"El resultado es {suma(n1,n2)}")
    if op == 2:
        # print("La funcion restar está en proceso. Unase a la beta")
        num1 = int(input("Ingresa el primer numero >> "))
        num2 = int(input("Ingresa el segundo numero >>> "))
        resta(num1,num2) 
       # print(f"El resultado es {resta(num1,num2)}")

menuCalculadora()