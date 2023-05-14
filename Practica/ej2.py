#Solicitar numeros al usuario hasta que ingrese el 0. Por cada uno, mostrar la suma de sus digitos (utilizando una funcion que realice dicha suma)

def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
        print(digito)
    return suma

numero = int(input("Ingrese un numero, 0 para terminar"))
while numero != 0:
    print("La suma de los digitos de ", numero, " es: ", suma_digitos(numero))
    numero = int(input('Ingrese un numero, 0 para terminar'))
    