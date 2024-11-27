'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
limite_inferior = int(input("Escribe el limite inferior: "))
limite_superior = int(input("Escribe el limite superior: "))

for i in range(limite_inferior,limite_superior + 1):
    if i % 2 == 0:
        print(i)