fname = input('Introduzaca el nombre del archivo: ')

try:
    fhand = open(fname)
except :
    print('El archivo no se puede abrir ', fname)
    exit()

# Ahora ya podemos recorres las lineas del archivo y seleccionar las de From
