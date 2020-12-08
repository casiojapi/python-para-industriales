#Se quiere realizar un programa para calcular cuántas figuritas es necesario comprar para
#completar el álbum (A medida que vamos completando el álbum, las figuritas que compramos tienen
#más posibilidades de estar repetidas).
#Para ello, realizar un programa que simule la compra de figuritas hasta completar el álbum
#(Se puede suponer que se compran de a una)y cuente la cantidad de figuritas compradas. 
#Repetir el ciclo 100 veces e indicar el promedio de figuritas compradas para completar el álbum.
#def buscar(figurita, album):


import random
def prog():
    album=[]
    cant_repetidas=[]
    cant_compradas=[]
    for i in range(0,100):
        figurita=random.randint(1,600)
        print(figurita)
        cant_compradas.append(figurita)
        for i in album
           if album[i]==figurita:
             cant_repetidas.append(figurita)
           else:
                album.append(figurita)
    print(album)       
    if (len(album))==600:
        print("Ha completado el album")
    elif (len(album)) < 600:
        print("No ha completado el album")
        faltan=600 - len(album)
        print("Le faltan", faltan, "figuritas")
    print("Ha comprado", len(cant_compradas), "figuritas en total")
    print("Tiene", len(cant_repetidas), "figuritas repetidas")
    print(cant_compradas)
    print(cant_repetidas)
prog()