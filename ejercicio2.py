'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''
import random
aleatorio = random.randint(1, 100)

intentos_totales = 10
intentos_realizados = 0

print ("Intenta adivinar un numero entre el 1 y el 100 en menos de 10 intentos")
while intentos_realizados < intentos_totales:
    intento = int(input("Introduce tu número: "))
    intentos_realizados += 1
    intentos_restantes = intentos_totales - intentos_realizados

    if intento == aleatorio:
        print(f"¡Felicidades! Has acertado el número en {intentos_realizados} intentos.")
        break
    elif intento < aleatorio:
        print(f"El número a adivinar es mayor. Te quedan {intentos_restantes} intentos.")
    else:
        print(f"El número a adivinar es menor. Te quedan {intentos_restantes} intentos.")

if intentos_realizados == intentos_totales and intento != aleatorio:
    print(f"Lo siento, se han agotado tus intentos. El número era {aleatorio}.")