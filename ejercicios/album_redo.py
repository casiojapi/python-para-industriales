#Se quiere realizar un programa para calcular cuántas figuritas es necesario comprar para
#completar el álbum (A medida que vamos completando el álbum, las figuritas que compramos tienen
#más posibilidades de estar repetidas).
#Para ello, realizar un programa que simule la compra de figuritas hasta completar el álbum
#(Se puede suponer que se compran de a una)y cuente la cantidad de figuritas compradas. 
#Repetir el ciclo 100 veces e indicar el promedio de figuritas compradas para completar el álbum.
#def buscar(figurita, album):


import random
def llenar_album(total_figuritas):
    album = []
    tengo = 0
    nola = True
    cant_compradas = 0
    while tengo < total_figuritas:
        figurita = random.randint(1, total_figuritas)
        cant_compradas += 1
        for i in range(tengo):
            nola = True
            if album[i] == figurita:
                nola = False
                break
        if nola:
            album.append(figurita)
            tengo += 1
    print("Ha comprado", cant_compradas, "figuritas en total")
    return cant_compradas

def main():
    sumatoria = 0
    cantidad_de_vueltas = 100
    for i in range(cantidad_de_vueltas):
        print(i)
        res = llenar_album(400)
        sumatoria += res
    promedio_compradas = sumatoria / cantidad_de_vueltas
    print("promedio: ", promedio_compradas)
    return
    
main()