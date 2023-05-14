def seguir():
    respuesta = ""
    while respuesta not in ['S', 's', 'N', 'n']:
        print("Desea realizar otro cromado? S/N")
        respuesta = input()
    return respuesta
capacidadmax = float(input("Ingrese la capacidad maxima del recipiente >> "))
estado = capacidadmax

while True:
    usando = float(input("Ingrese el liquido que se gastará para realizar el cromado >> "))
    
    if usando <= estado:
        print("Es posible realizar el cromado")
        estado -= usando
    else: print("No es posible realizar el cromado")
    
    print("Cantidad restante >> ", estado)
    
    if estado < (capacidadmax*0.20): print("La cantidad restante se encuentra por debajo del 20% de su capacidad")
    
    resp = seguir()
    
    if resp in ['N', 'n']:
        break