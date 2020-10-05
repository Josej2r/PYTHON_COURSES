d = dict()
fname = input('Introduzaca el nombre del archivo: ')

try:
    fhand = open(fname)
except :
    print('El archivo no se puede abrir ', fname)
    exit()

# Ahora ya podemos recorres las lineas del archivo y seleccionar las de From

for lineas in fhand:
    lineas = lineas.rstrip()

    if not lineas.startswith("From "):
        continue
    lineas = lineas.split(" ")
    fecha = lineas[6].split(":")
    # Ya tendríamos las horas separadas
    hora = fecha[0]

    # ahora tendríamos que crear un diccionario donde guardar las horas y su
    # numero de veces, es decir su contador
    d[hora] = d.get(hora, 0) + 1
# ya tenemos el diccionario con las horas y el numero de repeticiones,
# ahora tenemos que ordenarlas

lst_sin_orden = list(d.items())
lst_sin_orden.sort()

for hora, contador in lst_sin_orden:
    print(hora, contador)
