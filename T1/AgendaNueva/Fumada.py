#directorio = dict([tuple(line.split(',')) for line in directorio])
file = 'miagendahoy.txt'

#Creo la variable directorio que la convierto en una lista para meter dentro el contenido del fichero
directorio=[]

f = open(file, 'r')
directorio = f.readlines()
print("Compruebo el contenido de directorio: ",directorio," que es del tipo",type(directorio))

#creo una lista vacia y luego le pasare el contenido del fichero separado por comas
miLista=[] #creo una lista vacia
for line in directorio: #recorro todo el directorio, linea a linea
    miLista.append(line.split(','))#a mi lista, le añado (por el final) lo que voy leyendo de directorio y lo separo con comas {split}
    print("\n miLista pasada por el split devuelve: ", miLista," que sigue siendo del tipo",type(miLista))

print("\n\n\n\n por lo que de momento, la lista despues de leer el fichero ")
mitupla = tuple(miLista)

midict={}

#Examen ¿Como convierto algo en un diccionario? : Respuesta: con un dict

for i in range(len(mitupla)):
    print(mitupla[i], " i=",i)
    midict=dict(mitupla)

print("\n\nEl diccionario completo contiene: ",midict)


