personas=[]

unaPersona={}
unaPersona["nombre"]=input("Nombre")
unaPersona['dni']=int(input("DNI"))
unaPersona['notas']=[]
unaNota=int(input("Nota (cero para terminar)"))
while unaNota!=0:
    unaPersona['notas'].append(unaNota)
    unaNota=int(input("Nota (cero para terminar)"))
personas.append(unaPersona)