#Tuplas dentro de tupla

def tupla_dentro_de_tupla_y_dentro_de_lista():
    t1=((7,9,3),2,"Hola","Pedro")
    print(t1[0])
    for i in range(0,3):
        print(t1[0][i])
    for j in range(1,4):
        print(t1[j])
        
tupla_dentro_de_tupla_y_dentro_de_lista()