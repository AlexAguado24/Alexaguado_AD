numeros = [40, 21, 4, 9, 10, 35]

for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j],  numeros[i]
        else:
            numeros[i] = numeros[i]


print(numeros)
