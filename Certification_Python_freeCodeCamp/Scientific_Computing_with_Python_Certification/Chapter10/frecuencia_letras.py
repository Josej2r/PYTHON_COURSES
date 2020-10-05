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

# ELIMINAR NUMEROS DE LAS PALABRAS

    linea = linea.lower()
    palabras = linea.split()

    for palabra in palabras:
        d[palabra] = d.get(palabra, 0) + 1


# tendríamos un diccionario con las palbras y su frecuencia

# creamos tupla palabra, frecuencia

t = list(d.items())

lst_change = list()

for word, frecuency in t:
    lst_change.append((frecuency, word))

lst_change.sort(reverse=True)

lst_sorted = list()

for frecuency, key in lst_change:
    lst_sorted.append((key, frecuency))

print(lst_sorted)
