calendario = dict()

fname = input("Introduzca el nombre del archivo: ")

try:
    fhand = open(fname)
except:
    print("El archivo no se puede abrir", fname)
    exit()

for lineas in fhand:
    lineas = lineas.rstrip()

    if not lineas.startswith("From "):
        continue
    # ha este punto solamnte llegan las lineas que empiezan por From

    # Separamos las frases por palabras usando split()
    lineas = lineas.split(" ")
    palabra_dia = lineas[2]

    # ya tenemos el día guardado en palabra_dia ahora ya podemos ir creando el
    # diccionario

    calendario[palabra_dia] = calendario.get(palabra_dia, 0) + 1

    # OTRA MANERA DE AÑADIR LOS DIAS Y CONTAR CUANTOS HAY

    #if palabra_dia not in calendario:
        #calendario[palabra_dia] = 1
    #else:
        #calendario[palabra_dia] += 1

print(calendario)
