print("Creando fichero miagenda.txt")

miAgenda = "miagenda.txt"
try:
    with open(miAgenda, "w")as f:
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
        with open(miAgenda,"w")as f:
            f.close()

with open(miAgenda,"w")as f:
    f.write("")
    f.close()





