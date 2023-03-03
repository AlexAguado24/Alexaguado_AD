lista=[1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26]

def algoritmo (lista, n, izquierda, derecha):
    print("\n",lista)
    print("izquierda",izquierda)
    print("derecha",derecha)
    print("numero",n)
   
    if n> lista[len(lista)-1]:
        return("Nooo encontrado, mayor que el último de la lista")
   
    if izquierda > derecha:
        if n==izquierda:
            return "encontrado"
        else:
            return ("No encontrado")
   
    Indice_Medio = (izquierda + derecha) // 2
    Elemento_medio = lista[Indice_Medio]
   
    print("Elemento medio:",Elemento_medio)
    if Elemento_medio == n:
        return ("Encontrado")
    if n < Elemento_medio:
        return algoritmo(lista, n, izquierda, Indice_Medio - 1)
    else:
        return algoritmo(lista, n, Indice_Medio + 1, derecha)
   
print(lista[0])
print(len(lista))
print("---")
num=int(input("Buscar:"))
print(algoritmo(lista,num,lista[0],len(lista))) #lista,número a buscar, valor primero, longitud lista