#Matriz cuadrada random en 2D

import random
def main():
    l=[]
    M2D=[]
    n=int(input("Cantidad de elementos del vector:"))
    for i in range(n):
        l.append(0)
        M2D.append([])
        for j in range(n):
            M2D[i].append(random.randint(0,50))
    for i in range(n):
        for j in range(n):
            l[i]=l[i]+M2D[i][j]
    for i in range(n):
        print("l!",i,"l",l[i])
        for j in range(n):
            print("M2D!",i,"!!",j,"M",M2D[i][j])
            
main()          
        