'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''
limite_inferior = int(input("Escribe el limite inferior: "))
limite_superior = int(input("Escribe el limite superior: "))
suma = 0
contf = 0
conti = 0
while True:
    if limite_inferior >= limite_superior:
        limite_inferior =int(input('El limite inferior no puede ser mayor o igual al superior, REESCRIBELO: '))
    else:
        break
    
while True :
    n = int(input('Escribe un numero: '))
    if n == 0:
        break
    else: 
        if n == limite_inferior or n == limite_superior:
            conti += 1
        else:
            if n > limite_inferior and n < limite_superior:
                suma += n
            else:
                contf += 1
                