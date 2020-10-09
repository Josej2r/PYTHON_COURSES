import string
d = dict()
fname = input('Introduzaca el nombre del archivo: ')

try:
    fhand = open(fname)

except :
    print('El archivo no se puede abrir ', fname)
    exit()

# Ahora ya podemos recorres las lineas del archivo y seleccionar las de From

for linea in fhand:
    linea = linea.rstrip()  # quitamos los saltos de lineas

    linea = linea.translate(linea.maketrans('', '', string.punctuation))
    linea = linea.translate(linea.maketrans('', '', string.digits))
    linea = linea.lower()
    palabras = linea.split()

    for palabra in palabras:
        for letra in palabra:  # este es el que nos separa las palabras en letra
            d[letra] = d.get(letra, 0) + 1


# tendríamos un diccionario con las letra y su frecuencia

# creamos tupla letra, frecuencia


t = list(d.items())

lst_change = list()

for letter, frecuency in t:
    lst_change.append((frecuency, letter))

lst_change.sort(reverse=True)

lst_sorted = list()

for frecuency, key in lst_change:
    lst_sorted.append((key, frecuency))

for x in lst_sorted:
    print(x)
