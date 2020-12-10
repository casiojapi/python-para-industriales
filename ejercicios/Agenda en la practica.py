def ejemplo():
    agenda = []
    opcion = 0
    #abrir el archivo para lectura, leer todos los datos y cerrarlo
    while opcion != 4:
        print("1-Cargar contacto")
        print("2-Buscar contacto")
        print("3-Mostrar agenda")
        print("4-Salir")
        opcion = int(input("Ingrese su opción:"))
    
        if opcion == 1:
            contacto = {}
            contacto["nombre"] = input("Ingrese el nombre:")
            contacto["apellido"] = input("Ingrese el apellido:")
            contacto["calle"] = input("Ingrese la calle:")
            contacto["numero"] = int(input("Ingrese el numero:"))
            contacto["telefono"] = input("Ingrese el telefono:")
            contacto["celular"] = input("Ingrese el celular:")
            contacto["email"] = input("Ingrese el email:")
            agenda.append(contacto)
        elif opcion ==2:
            ape = input("Ingrese el apellido a buscar:")
            for i in agenda:
                if i["apellido"] == ape:
                    print(i["email"])
            print()
        elif opcion ==3:
            for i in agenda:
                for dato in i:
                    print (dato, ":", i[dato])
                print()
    #abrir el archivo para escritura, escribo todos los datos y lo cierro   
ejemplo()