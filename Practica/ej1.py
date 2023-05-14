# 1 Solicitar al usuario que ingrese su direccion email. Imprimir un mensaje indicando si la dirección es válida o no
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo @

def valido(email):
    if "@" in email:
        print("Direccion valida")
    else: print("Direccion invalida")

email = input("Ingrese su dirección email >> ")

valido(email)
