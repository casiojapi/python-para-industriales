#Lista con promedio
def prog():
    l=[]
    cant=int(input("Ingrese la cantidad de valores:"))
    suma=0
    for i in range(0,cant):
        a=int(input("Ingrese valor de la lista:"))
        l.append(a)
        suma=suma + l[i]
    prom=suma/(cant)
    print("El promedio es:",round(prom,2))
    #Round es para redondear, en este caso 2 decimales quiero
    
prog()
    