from random import randint
  
def guido():
    lista = []
    for i in range (0,20):
        lista.append(randint(0,100))
    perdio = False
    x=0
    while x<20 and perdio == False:
        print(lista[x])
        rta = input("mayor o menor (y/n)")
        if (rta == "y" and lista[x+1]>lista[x]) or (rta == "n" and lista[x+1]<lista[x]):
            print("Correcto")
            x = x+1
        else:
            perdio = True
    print(lista)
    if perdio == False:
        print ("felicitaciones")
    else:
        print("Mejor suerte la proxima")
        
guido()