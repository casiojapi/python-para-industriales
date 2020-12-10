def main():
    lista_alumnos = []
    opcion = 0
    #abrir el archivo para lectura, leer todos los datos y cerrarlo
    while opcion != 4:
        print("1 - Cargar alumno")
        print("2 - Buscar alumno")
        print("3 - cantidad de alumnos a recurperar")
        print("4 - mejor promedio")
        opcion = int(input("Ingrese su opción:"))
    
        if opcion == 1:
            alumno = {} 
            alumno["padron"] = input("Ingrese el padron: ")
            alumno["nombre"] = input("Ingrese el nombre: ")
            alumno["apellido"] = input("Ingrese el apellido: ")
            alumno["codigo"] = input("Ingrese el codigo: ")
            alumno["nota_prim"] = int(input("Ingrese la primera nota: "))
            alumno["nota_segun"] = int(input("Ingrese la segunda nota: "))
            alumno["aprobo"] = input("Ingrese \"Si\" si aprobo la materia, o \"No\" si no ")
            lista_alumnos.append(alumno)

        elif opcion == 2:
            padron = input("Ingrese el padron del alumno que desea buscar:")
            no_esta = True
            for i in lista_alumnos:
                if i["padron"] == padron:
                    no_esta = False
                    print(i)
            if no_esta:
                print("El padron ingresado no se encuentra en la lista.")

        elif opcion == 3:
            tp = 0
            prim = 0
            segun = 0
            for i in lista_alumnos:
                if i["nota_prim"] < 4:
                    prim += 1
                if i["nota_segun"] < 4:
                    segun += 1
                if i["aprobo"] == "No":
                    tp += 1
            print("cantidad de alumnos que reprobaron tp: ", tp, "el primer parcial: ", prim, "el segundo parcial: ", segun)
        
        elif opcion == 4:
            mejor_promedio = 0
            mejores_alumnos = []
            for i in alumno:
                promedio = (i["nota_prim"] + i["nota_segun"]) / 2
                if promedio > mejor_promedio:
                    mejor_promedio = promedio
            for i in alumno:
                promedio = (i["nota_prim"] + i["nota_segun"]) / 2
                if promedio == mejor_promedio:
                    mejores_alumnos.append(i)
            for i in mejores_alumnos:
                print("Estos son los alumnos con los mejores promedios: ")
                print(i["nombre"], i["apellido"])


                
    #abrir el archivo para escritura, escribo todos los datos y lo cierro   
main()

# -	Cantidad de alumnos a recuperar: El programa deberá indicar para cada parcial, la cantidad de alumnos que obtuvieron nota menor a 4, y para el TP la cantidad de alumnos que no aprobaron.

# Mejor promedio: El programa deberá indicar el nombre del alumno que obtenga el mayor promedio. Si hay más de uno, deberá indicarlos todos.