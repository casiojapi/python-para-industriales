contacto = {}

contacto["nombre"] = input("Ingrese el nombre:")
contacto["apellido"] = input("Ingrese el apellido:")
contacto["calle"] = input("Ingrese la calle:")
contacto["numero"] = int(input("Ingrese el numero:"))
ontacto["telefono"] = input("Ingrese el telefono:")
contacto["celular"] = input("Ingrese el celular:")
contacto["email"] = input("Ingrese el email:")

print(contacto)

for dato in contacto:
    print (dato, ":", contacto[dato])