secret_number = 0

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

adivinar = True

while adivinar:
    secret_number = int(input("Ingresa un numero, y ve si puedes adivinarlo."))
    
    if secret_number == 777:
        print(f"Has adivinado, el numero secreto era {secret_number}")
        adivinar = False
    else:
        print("NO")

