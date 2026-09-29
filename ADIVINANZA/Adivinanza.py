import random

MINIMO = 1
MAXIMO = 1000
INTENTOS = 0

desconocido = random.randint(MINIMO, MAXIMO)

while True:
    num_usuario = int(input("Tu numero es: "))
    INTENTOS += 1
    if num_usuario > desconocido:
        print(f"Ese no es el numero... el numero es menor a {num_usuario}")
    elif num_usuario < desconocido:
        print(f"Ese no es el numero... el numero es mayor a {num_usuario}")
    else:
        break

    print(f"ESE ES EL NUMERO CORRECTO!, has tenido {INTENTOS} intentos")
