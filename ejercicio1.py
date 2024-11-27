'''
Ejercicio 1:
    Crea una programa que pida un número y calcule su factorial (El factorial de 
    un número es el producto de todos los enteros entre 1 y el propio número y se 
    representa por el número seguido de un signo de exclamación. 
    Por ejemplo 5! = 1x2x3x4x5=120)
'''
num = int (input ("Ingresa un número: "))
factorial = 1
if num < 0:
    print ("Error el factorial no se realiza en números negativos")
elif num == 0:
    print ("El factorial de 0 es 1")
else:
    for i in range (1, num + 1):
        factorial *= i
    print (f"El factorial de {num} es {factorial} ")