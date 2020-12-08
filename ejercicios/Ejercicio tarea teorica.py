def prog():
    cant_personas = 0
    personas=[]
    una_persona={}
    
    una_persona["Nombre"]=input("Nombre: ")
    una_persona['DNI']=int(input("DNI: "))
    una_persona["Notas"]=[]
    una_nota=int(input("Nota (cero para terminar)"))
    while una_nota!=0:
        una_persona['Notas'].append(una_nota)
        una_nota=int(input("Nota (cero para terminar)"))
        cant_personas = cant_personas + 1
    personas.append(una_persona)
    print(personas)
    una_persona={}
    for i in range (0,2):
        una_persona["Nombre"]=input("Nombre: ")
        una_persona['DNI']=int(input("DNI: "))
        una_persona['Notas']=[]
        una_nota=int(input("Nota (cero para terminar)"))
        while una_nota!=0:
            una_persona['Notas'].append(una_nota)
            una_nota=int(input("Nota (cero para terminar)"))
            cant_personas = cant_personas + 1
        personas.append(una_persona)
        print(personas)
    for p in personas:
        print(p["Nombre"])
        sum_nota=0
        for nota in p["Notas"]:
            sum_nota += nota
        print(sum_nota/len(p["Notas"]))
          
prog()