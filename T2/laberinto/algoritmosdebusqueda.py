#Burbuja
''' def ord_burbuja(array):
    n = len(array)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)

print(elementos) '''

#Insertion Sort:
''' def alg_InsertSort(array):
     
    if (n := len(array)) <= 1:
        return
   
    for i in range(1, n):        
        key = array[i]
        j = i-1
        while j >=0 and key < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key 
 
 
lista = [40,21,4,9,10,35]
alg_InsertSort(lista)
print(lista) '''


#Merge Sort
# Función merge_sort
''' def merge_sort(lista):
 
   """
   Lo primero que se ve en el psudocódigo es un if que
   comprueba la longitud de la lista. Si es menor que 2 (1 ó 0) se devuelve la lista.
   ¿Por que? Ya esta ordenada.
   """
   if len(lista) < 2:
      return lista
   
    # De lo contrario, se divide en 2
   else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)
        #return(merge(merge_sort(lista[:middle]),merge_sort(lista[middle:])))
   
# Función merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
 
   # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
 
    # Retornamos el resultados
    return result

# Prueba del algoritmo

lista = [40,21,4,9,10,35] 


merge_sort_result = merge_sort(lista)  
print(merge_sort_result)
print(merge_sort(lista)) '''


#Quick Sort
''' def Partir(vector, bajo, alto):
    i = (bajo-1)    
    pivote = vector[alto]
    for j in range(bajo, alto):
        if vector[j] <= pivote:
            i = i+1
            vector[i], vector[j] = vector[j], vector[i]
    vector[i+1], vector[alto] = vector[alto], vector[i+1]
    return (i+1)
 
 
def QuickSort(vector, bajo, alto):
    if len(vector) == 1:
        return vector
    if bajo < alto:
        vector_partido = Partir(vector, bajo, alto)
        QuickSort(vector, bajo, vector_partido-1)
        QuickSort(vector, vector_partido+1, alto)
 
 
vector = [10,7,8,9,1,5,4,12,25,65,3,2,6]
n = len(vector)

print("El vector SIN ordenar es:")
print(vector)
   
QuickSort(vector, 0, n-1)

print("\nEl vector ordenado es:")
print(vector) '''