direcciones_correo = dict()

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
    correo = lineas[1]  # tomamos la direccion de correo
    direcciones_correo[correo] = direcciones_correo.get(correo, 0) + 1

    # Ahora tenemos un diccionarios con las direcciones de correo y el número
    # de correos que a mandado cada persona
