direcciones = dict()

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
    palabra_direccion = lineas[1]

# ya tenemos el día guardado en palabra_direccion ahora ya podemos ir creando el
# diccionario

    direcciones[palabra_direccion] = direcciones.get(palabra_direccion, 0) + 1

direccion_veces = None  # sera el numero de veces el valor de la clave
direccion_nombre = None  # sera la clave


for clave, contador in direcciones.items():

    if direccion_veces is None or contador > direccion_veces:
        direccion_nombre = clave
        direccion_veces = contador
print(direccion_nombre, direccion_veces)
