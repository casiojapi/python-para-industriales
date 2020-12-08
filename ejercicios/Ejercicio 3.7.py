#Ejercicio 3.7
"""
Construir un algoritmo que para cada auto participante en una carrera, lea un número
de auto y el tiempo de vuelta (en segundos y centésimas, se ingresan por separado).
Previamente se debe leer la longitud del circuito. Dada una serie de números de autos leídos
a continuación, se deben informar las velocidades promedio correspondientes a cada tiempo
de vuelta de dichos autos. Ambos conjuntos de datos se terminan con un código de auto
negativo
"""

def main():
    d=int(input('longitud del circuito [m]:'))
    auto=[]
    seg=[]
    cen=[]
    vel=[]
    tiempo=[]
    a=int(input('auto nº:'))
    auto.append(a)
    s=int(input('segundos:'))
    seg.append(s)
    c=int(input('centesimas:'))
    cen.append(c)
    
    while a>0:
        a=int(input('auto nº:'))
        if a>0:
            auto.append(a)
            s=int(input('segundos:'))
            seg.append(s)
            c=int(input('centesimas:'))
            cen.append(c)
    
    for i in range (len(auto)):
        t=seg[i]+(cen[i]/100)
        tiempo.append(t)
        v=d/tiempo[i]
        vel.append(v)
    d=[d]*len(auto)
    
    print('auto nº distancia  tiempo  velocidad')
    for p in range (len(auto)):
        print('   ',auto[p],'    ',d[p],'    ',tiempo[p],'   ',round(vel[p],2))      
main()

