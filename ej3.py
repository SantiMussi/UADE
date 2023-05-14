#Funciones
def seguir():
    respuesta = ''
    while respuesta not in ['S', 's', 'N', 'n']:
        print('Desea ingresar otro estudiante? S/N')
    return respuesta

#Variables globales
more_pants = ''
pantalonesmax = 0
mujeres = 0
hombres = 0

#Inicio del proceso de identificacion
while respuesta not in ['S', 's', 'N', 'n']:
    respuesta = input('Desea realizar un proceso? S/N >> ')

while respuesta in ['S', 's']:
    #Reset de variables
    camisas = 0
    pantalones = 0
    vestidos = 0
    otros = 0
    sexo = 0
    
    #Descripcion del estudiante, etc.
    nombre = input('Ingrese el nombre del estudiante: ')
    while sexo not in [1, 2]:
        sexo = int(input('Ingrese el sexo del estudiante (1 = Masculino, 2 = Femenino) >> '))
    prendas = int(input('Ingrese la cantidad de prendas que trae >> '))
    
    for i in range(prendas):
        descripcion = 0
        while descripcion not in [1,2,3,4]:
            descripcion = int(input('Ingrese la descripcion de la ropa (1- Camisa, 2- Pantalon, 3- Vestido, 4- Otro) >> '))
        
        if descripcion == 1:
            camisas +=1
        if descripcion == 2:
            pantalones +=1
        if descripcion == 3:
            vestidos +=1
        if descripcion == 4:
            otros +=1
    
    #Ejercicio 1
    print('El estudiante dejo ', camisas, ' camisas')
    print('El estudiante dejo ', pantalones, ' pantalones')
    
    #Ejercicio 2
    if camisas > 5:
        if pantalones >= pantalonesmax:
            more_pants = nombre
    
    #Ejercicio 3 parte 1
    if sexo == 1:
        hombres +=1
    if sexo == 2:
        mujeres +=1
    
    total = camisas*0.450 + pantalones*0.650
    
    print('El estudiante entrego ', total, ' kilogramos de camisas y pantalones en total')
    respuesta = seguir()

#Ejercicio 3 parte 2
if hombres > mujeres:
    print('La lavanderia es menos utilizada por las mujeres')
elif mujeres > hombres:
    print('La lavanderai es menos utilizada por los hombres')
else: print('La lavanderia es utilizada por igual')