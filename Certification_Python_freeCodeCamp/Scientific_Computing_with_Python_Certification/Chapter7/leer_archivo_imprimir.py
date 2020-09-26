nombre_archivo = input("Introduzca el nombre del archivo: ")
manejador_archivo = open(nombre_archivo, 'r')

for lineas in manejador_archivo:
    lineas = lineas.rstrip()  # Para eliminar el espacio en blanco a la derecha
    #  final de las lineas
    print(lineas.upper())
