#Operaciones con tuplas y listas

def operaciones_con_tuplas_y_listas():
    list1=[9,-2,7,12]
    #Tuple pasa una lista a tupla
    tup1=tuple(list1)
    print("Lista 1:",list1)
    print("Tupla 1:",tup1)
    tup2=tuple(x**2 for x in tup1)
    print("Tupla2:",tup2)
    #list pasa una tupla a lista
    list2=list(tup2)
    print("Lista 2:",list2)
    
operaciones_con_tuplas_y_listas()


"""
Las tuplas tienen datos no necesariamente del mismo tipo, dentro del parentesis, separado por comas
Las listas tienen datos del mismo tipo, dentro de corchetes, separados por comas
"""

def tuplas_y_listas():
    tup1=(1.23,"Hola",20)
    print("Tupla 1:" ,tup1)
    list1=[3,7,9,10]
    print("Lista 1:" ,list1)
    
tuplas_y_listas()