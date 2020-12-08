contacto = {}
fecha = {}
contacto["nombre"] = input("Ingrese el nombre:")
contacto["apellido"] = input("Ingrese el apellido:")
contacto["calle"] = input("Ingrese la calle:")
contacto["numero"] = int(input("Ingrese el numero:"))
contacto["telefono"] = input("Ingrese el telefono:")
contacto["celular"] = input("Ingrese el celular:")
contacto["email"] = input("Ingrese el email:")

fecha["dia"] = int(input("Ingrese el día de nacimiento:"))
fecha["mes"] = int(input("Ingrese el mes de nacimiento:"))
fecha["anio"] = int(input("Ingrese el año de nacimiento:"))
contacto["fecha_nac"] = fecha