import random

def buscar(l,elem):
    for i in range(0,len(l)):
        if l[i] == elem:
            return i
    return -1
"""
def buscar(l,elem):
    r=-1
    for i in range(0,len(1)):
        if l[i] == elem:
            r= i
    return r
"""       


def prog():
    lista=[]
    cant=int(input("Ingrese la cantidad de elementos:"))
    for i in range(0,cant):
        n=random.randint(0,100)
        lista.append(n)
    x = int(input("Ingrese un numero del 0 al 100:"))
    r = buscar(lista,x)
   
   if r == -1:
       print(" El elemento no esta en la lista ")
   else:
        print(" El elemento esta en la posicion",i)
   print(lista)
        
prog()
    