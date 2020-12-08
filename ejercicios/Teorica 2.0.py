alumno=[]

unAlumno={}
unAlumno["nombre"]=input("Nombre:")
unAlumno["apellido"]=input("Apellido:")
unAlumno['dni']=input("DNI:")
unAlumno["padron"]=input("Padron:")
unAlumno['notas']=[]
unaNota=int(input("Nota: (cero para terminar)"))
while unaNota!=0:
    unAlumno['notas'].append(unaNota)
    unaNota=int(input("Nota (cero para terminar)"))
alumno.append(unAlumno)