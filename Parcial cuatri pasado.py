
"""
[equipo1,equipo2,equipo1]
{
    clave: Value
    nombre_equipo: [puntos, partidos_jugados, goles_favor, goles_contra, diferencia_goles]

    boca: [puntos, partidos_jugados, goles_favor, goles_contra, diferencia_goles]
    river: [puntos,partidos_jugados, goles_favor, goles_contra, diferencia_goles]
    lanus: [puntos,partidos_jugados, goles_favor, goles_contra, diferencia_goles]
    


}
"""
def ingresar_resultado_del_partido(dic):

    nombre_equipo_uno = input("Ingrese equipo 1 ")
    nombre_equipo_dos = input("Ingrese equipo 2 ")

    goles_primer_equipo = int( input("Ingrese goles del primer equipo ") )
    goles_segundo_equipo = int( input("Ingrese goles del segundo equipo ") )

    lista_equipo_uno = dic[nombre_equipo_uno]
    lista_equipo_dos = dic[nombre_equipo_dos]


    #puntos
    if goles_primer_equipo > goles_segundo_equipo:
        lista_equipo_uno[0] = lista_equipo_uno[0] + 3
    elif goles_primer_equipo < goles_segundo_equipo:
        lista_equipo_dos[0] = lista_equipo_dos[0] + 3
    else:
        lista_equipo_uno[0] = lista_equipo_uno[0] + 1
        lista_equipo_dos[0] = lista_equipo_dos[0] + 1

    #partidos jugadios
    lista_equipo_uno[1] = lista_equipo_uno[1] + 1
    lista_equipo_dos[1] = lista_equipo_dos[1] + 1
    #goles a favor
    lista_equipo_uno[2] = lista_equipo_uno[2] + goles_primer_equipo
    lista_equipo_dos[2] = lista_equipo_dos[2] + goles_segundo_equipo
    #goles en contra
    lista_equipo_uno[3] = lista_equipo_uno[3] + goles_segundo_equipo
    lista_equipo_dos[3] = lista_equipo_dos[3] + goles_primer_equipo
    #diferencia de gol
    lista_equipo_uno[4] = lista_equipo_uno[2] - lista_equipo_uno[3]
    lista_equipo_dos[4] = lista_equipo_dos[2] - lista_equipo_dos[3]



"""

nombre_equipo   puntos   partidos_jugados    goles_favor     goles_contra    diferencia_goles

tabla = [
[n_equipo, puntos, partidos_jugados, goles_favor, goles_contra, diferencia_goles]
[n_equipo, puntos, partidos_jugados, goles_favor, goles_contra, diferencia_goles]
[n_equipo, puntos, partidos_jugados, goles_favor, goles_contra, diferencia_goles]
[n_equipo, puntos, partidos_jugados, goles_favor, goles_contra, diferencia_goles]
[n_equipo, puntos, partidos_jugados, goles_favor, goles_contra, diferencia_goles]
]


lista.sort(diferencia_goles)
lista.sort(puntos)


"""
def por_diferencia(l):
    return l[5]

def por_puntos(l):
    return l[1]

def mostrar_tabla(dic):
    tabla = []

    for clave in dic:
        lista_equipo = dic[clave]
        tupla = (clave, lista_equipo[0],lista_equipo[1],lista_equipo[2],lista_equipo[3], lista_equipo[4])

        tabla.append(tupla)
    
    tabla.sort(reverse= True, key= por_diferencia)
    tabla.sort(reverse= True, key= por_puntos)

    for equipo in tabla:
        print(equipo)


def ejercicio_parcial():
    diccionario_equipos = {}
    cantidad_equipo = int( input("Ingrese cantidad de equipos ") )

    for numero_de_equipo in range(cantidad_equipo):
        nombre_equipo = input("Ingrese nombre del equipo ")
        diccionario_equipos[nombre_equipo] = [0,0,0,0,0]

    opcion = int( input("Ingrese opcion ") )

    while opcion != 3:

        if opcion == 1:
            ingresar_resultado_del_partido(diccionario_equipos)

        if opcion == 2:
            mostrar_tabla(diccionario_equipos)

        opcion = int( input("Ingrese opcion ") )

    #termine bro

        
ejercicio_parcial()
