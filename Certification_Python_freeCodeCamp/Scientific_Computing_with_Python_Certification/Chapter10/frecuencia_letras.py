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
    linea = linea.lower()

    if len(linea) == 0:
        continue

    palabras = linea.split()

    # tenemos una lista con las palabras de cada lineas
    for i in range(len(palabras)):
        letra = list(palabras[i])
        print(letra)
        d[letra] = d.get(letra, 0) + 1
        print(d)

# TENEMOS QUE ELIMINAR LAS LINEAS EN BLANCO
