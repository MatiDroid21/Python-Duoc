import os
import time

num1 = 1
num2 = 1
def suma(num1,num2):
    return int(num1) + int(num2)

def resta(num1,num2):
    return int(num1) - int(num2)

def multip(num1,num2):
    return int(num1) * int(num2)

def div(num1,num2):
    return int(num1) / int(num2)

os.system("cls")
print("=== calculadora de dos numeros ===")

try:
    num1 = float(input("Ingrese n1 >>> "))
    num2 = float(input("Ingrese n2 >>> "))
except:
        print("Se esperaba un numero")
        time.sleep(1)
        os.system("cls")

print("validando.")
time.sleep(1)
print("validando..")
time.sleep(2)
print("validando...")
time.sleep(1)
os.system("cls")
print("===========================")

print(f"la suma de {num1} y {num2} es igual a: {suma(num1,num2)}")

print("===========================")

print(f"la resta de {num1} y {num2} es igual a: {resta(num1,num2)}")

print("===========================")

print(f"la multiplicacion de {num1} y {num2} es igual a: {multip(num1,num2)}")

print("===========================")

print(f"la division de {num1} y {num2} es igual a: {float(div(num1,num2))}")

