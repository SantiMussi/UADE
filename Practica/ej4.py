#Solicitar al usuario el ingreso de numeros primos. La lectura finalizara cuando ingrese un numero que no sea primo. Por cada numero,
#mostrar la suma de sus digitos. Tambien solicitar al usuario un digito e informar la cantidad de veces que aparece en el numero. Al finalizar
#el programa, mostrar el factorial del mayor numero ingresado

from math import factorial

mayor = -9999999999999

#Tecnica de Prueba de divisibilidad
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

while True:
    numero = int(input('Ingrese un numero primo >> '))
    
    if es_primo(numero) == False:
        print('El numero no es primo, saliendo...')
        break
    
    suma = 0
    count = 0
    if mayor < numero:
        mayor = numero
            
    for digito in str(numero):
        suma += int(digito)
    print('La suma de sus digitos es >> ', suma)
        
    digit = input('Ingrese un digito para informarle la cantidad de veces que aparece en el numero ingresado >> ')
        
    for i in str(numero):
        if i == digit:
            count +=1
        
    print('El digito aparece ', count, ' veces')
        
print('El factorial del mayor numero ingresado es >> ', factorial(mayor))