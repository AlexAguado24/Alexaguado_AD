
fichero="ficheroexam4.txt"


with open ("ficheroexam3.txt", "r") as f:
    contenido = f.readlines
    f.close
    
with open ("ficheroexam3.txt", "w") as f:
    contenido = dict([tuple(line.split(',')) for line in contenido])
    



def consulta_errores(fichero):
    try:
        with open(fichero, "r") as f:
            contenido = f.readlines
            f.close()
            print(contenido)
    except FileNotFoundError:
        print("El fichero no existe")
    

def menu():
    print("1.Consulta Errores")
    print("2.Existe Error")
    print("3.Borrar Errores")
    print("4.Salir")
    opcion = input("Introduce la opcion que desees \n")
    return opcion


def ejecutar_menu():
    
    while True:
        opcion=int(menu())
        if opcion == 1:
            print("Consulta de Errores")
            consulta_errores(fichero)
        elif opcion == 2:
            print("Existe Error")
        elif opcion == 3:
            print("Borrando Errores")
        elif opcion == 4:
            print("ciao")
            break
        

print("Ejecitando programa")
ejecutar_menu()

    