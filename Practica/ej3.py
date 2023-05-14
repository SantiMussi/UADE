#Escribir un programa que pida numeros al usuario, mostrar el factorial de cada uno y, al finalizar, la cantidad total de numeros leidos en total.
#Utilizar una o mas funciones, segun sea necesario

from math import factorial

def seguir():
    resp = ''
    while resp not in ['S', 's', 'N', 'n']:
        print('Desea continuar? S/N')
        resp = input()
    return resp

count = 0

while True:
    count +=1
    numero = int(input('Ingrese un numero > '))
    print("El factorial es >> ", factorial(numero))    
    respuesta = seguir()
    if respuesta in ['N', 'n']:
        break

print('La cantidad total de numeros leidos >> ', count)