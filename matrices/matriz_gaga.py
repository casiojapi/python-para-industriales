def Matrices():
    m=5 #Cantidad de filas
    n=3 #Cantidad de columnas
    mat = []  #Crear la matriz
    for i in range(0,m):
        mat.append([]) #Crear las filas de la matriz
        for j in range(0,n):
            mat[i].append(int(0))
    TotVend = []
    TotSuc = []
    nom = []
    dni = []
    for i in range(0,m):
        TotVend.append(0)
    for j in range(0,n):
        TotSuc.append(0)
    for i in range(0,m):
        nombre=input("Ingrese nombre del vendedor:")
        doc=int(input("Ingrese su DNI:"))
        nom.append(nombre)
        dni.append(doc)
    op=0
    while op!=4:
        print("MENU PRINCIPAL")
        print("1-Ingresar una venta")
        print("2-Total por sucursal")
        print("3-Listado de vendedores")
        print("4-Salir.")
        op=int(input("Ingrese opción:"))
        if op==1:
            ingresar_venta(mat,dni)
        elif op==2:
            total_sucursal(mat,TotSuc)
        elif op==3:
            listado_vendedores(mat,TotVend,nom,dni)
             
Matrices()