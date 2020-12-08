"""
Las figuritas del mundial.

El álbum de figuritas del Mundial tiene aproximadamente 600 figuritas. Se sabe que no hay figuritas difíciles
(todas las figuritas tienen la misma posibilidad de salir).

Se quiere realizar un programa para calcular cuántas figuritas es necesario comprar para completar el álbum
(A medida que vamos completando el álbum, las figuritas que compramos tienen más posibilidades de estar repetidas).

Para ello, realizar un programa que simule la compra de figuritas hasta completar el álbum
(Se puede suponer que se compran de a una)y cuente la cantidad de figuritas compradas. 

Repetir el ciclo 100 veces e indicar el promedio de figuritas compradas para completar el álbum.

"""
import random
from random import randrange
def figuritas():
    
    album  = []
    
    cont_compr = 0
    
    for i in range (0,100): #repite el ciclo del programa 100 veces
        #acá empieza el programa en sí
        repetidas = 0
        compradas = 0
        
        for i in range (0,600): 
            album.append(i+1)
        while album != []:
            r = randrange(1,601)
            #print(album)
            if r in album:
                album.pop(album.index(r))
                compradas += 1
            else:
                compradas += 1
                repetidas += 1
        print (compradas)
        # fin del programa
        cont_compr += compradas # cuenta las compradas para después calcular el promedio
    promedio = cont_compr/100
    
    print("En promedio, usted necesitará comprar",promedio,"figuritas para completar el álbum")
    
figuritas()
        
