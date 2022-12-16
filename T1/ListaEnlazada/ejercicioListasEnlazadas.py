listaGrande = []


def crear_nodo():
    nodo = []
    valor2 = 0
    valor1 = int(input("Introduce un valor\n"))
    nodo.append(valor2)
    nodo.append(valor1)
    return nodo


def insertar_nodo(lista,nodo):
    lista.append(nodo)
    lista.sort()
    print(lista)
    return lista


def menu():
    print("1. Crear nodo")
    print("2. Insertar nodo")
    print("3. Eliminar nodo")
    print("4. Buscar nodo")
    print("5. Contar nodo")
    opcion = input("Introduce la opcion deseada\n")
    return opcion


def borrar_nodo():
    pass


def buscar_nodo():
    pass


def lanzar_programa():
    while True:
        opcion = str(menu())
        if opcion == str("1"):
            crear_nodo()
        elif opcion == str("2"):
            valor = crear_nodo()
            insertar_nodo(listaGrande,valor)
        elif opcion == 3:
            borrar_nodo()
        elif opcion == 4:
            buscar_nodo()
        else:
            break

lanzar_programa()