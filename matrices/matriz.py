#Ejercicio de matriz
import random

def matriz():
    m = 4 #Cantidad de filas
    n = 6 #Cantidad de columnas
    matriz = []
    for i in range(0,m):
        matriz.append([])
        for j in range(0,n):
            matriz[i].append(random.randint(0,99))
    for i in range(0,m):
        print(matriz[i])
        
    acum = []
    for j in range(0,n):
        acum.append(0)
    for i in range(0,m):
        for j in range(0,n):
            acum[j]=acum[j]+matriz[i][j]
    print()
    print(acum)
    
    maxi = acum[0]
    posmaxi = 0
    for j in range(1,n):
        if acum[j]>maxi:
            maxi = acum[i]
            posmaxi = j
    print(" El mejor vendedor es: ",posmaxi," que vendio: ",maxi)
matriz()