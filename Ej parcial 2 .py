def ejercicio_parcial_dos():
    lista = []

    for i in range(0,100):

        diccionario_figuritas = {}
        cantidad_figuritas_compradas = 0

        while len(diccionario_figuritas) != 600:

            numero_figurita = random.randint(1,600)

            if not numero_figurita in diccionario_figuritas:
                diccionario_figuritas[numero_figurita] = 0

            cantidad_figuritas_compradas = cantidad_figuritas_compradas + 1

        lista.append(cantidad_figuritas_compradas)

    #este punto
    cantidad_total = 0
    for cantidad_por_persona in lista:
        cantidad_total = cantidad_total + cantidad_por_persona
    
    promedio = cantidad_total / 100

    print(promedio)
    
    
ejercicio_parcial_dos()

Enviar mensaje a #general