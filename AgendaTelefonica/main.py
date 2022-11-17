MiAgenda = {
    'Nombre':'','Telefono':''
}
def crearFichero():
    print("Creando fichero miagenda.txt")

    miAgenda = "miagenda.txt"
    try:
        with open(miAgenda, "w") as f:
            f.close()
        if miAgenda:
            vacio = str(input("¿quieres dejarlo vacio?\n"))
            if vacio == "si":
                f = open(miAgenda, "w")
                f.write("")
                f.close()
    except FileNotFoundError:
        respuesta = str(input("El fichero no existe, ¿quieres crearlo?\n"))
        if respuesta == "si":
            with open(miAgenda, "w") as f:
                f.close()

def aniadirContacto(miAgenda):
    nombre = str(input("Escribe el nombre del contacto"))
    telefono = str(input("Escribe el numero del contacto"))
    MiAgenda['Nombre']= nombre
    MiAgenda['Telefono']= telefono
    with open(miAgenda, "a") as f:
        f.write(MiAgenda['Nombre'])
        f.write(',')
        f.write(MiAgenda['Telefono'])
        f.close()

def consultarTelefono():
    nombre = str(input("Indica el nombre del propietario del telefono"))


crearFichero()
aniadirContacto()





