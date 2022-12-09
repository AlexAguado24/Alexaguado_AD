
edadNum= int(input("Escribe la edad de Harry Potter: "))
edad= str()


MiDiccionario={
    'Nombre':'Harry',
    'Apellido':'Potter',
    'edad':'',
}

decenas=int((edadNum%100-edadNum%10)/10)
unidades=int(edadNum%10)

def unidades():
    if unidades == 1:
        edad = 'un'
    elif unidades == 2:
        edad = 'dos'
    elif unidades == 3:
        edad = 'tres'
    elif unidades == 4:
        edad = 'cuatro'
    elif unidades == 5:
        edad = 'cinco'
    elif unidades == 6:
        edad = 'seis'
    elif unidades == 7:
        edad = 'siete'
    elif unidades == 8:
        edad = 'ocho'
    elif unidades == 9:
        edad = 'nueve'
    return edad
        
def calculoDecenas():
    if(decenas == 1):
        if unidades == 0:
            edad = 'diez'
        elif unidades == 1:
            edad = 'once'
        elif unidades == 2:
            edad = 'doce'
        elif unidades == 3:
            edad = 'trece'
        elif unidades == 4:
            edad = 'catorce'
        elif unidades == 5:
            edad = 'quince'
        #elif 
    return edad




numero = input()
calculoDecenas(numero)

'''MiDiccionario['edad']= edad
print(calculoDecenas(MiDiccionario[edad]))'''