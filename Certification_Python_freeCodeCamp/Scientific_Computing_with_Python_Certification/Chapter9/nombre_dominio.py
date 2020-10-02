dominio = dict()

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
    palabra_dia = lineas[1]  # tomamos la direccion de correo
    palabra_dia = palabra_dia.split("@")
    dominio_dir = palabra_dia[1]
    dominio[dominio_dir] = dominio.get(dominio_dir, 0) + 1

print(dominio)
