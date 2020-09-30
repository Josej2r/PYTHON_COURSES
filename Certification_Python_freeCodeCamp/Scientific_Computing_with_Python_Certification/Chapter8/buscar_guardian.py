def buscar_dias():
    manejador_archivo = open("mbox-short.txt")
    for linea in manejador_archivo:
        palabras = linea.split()
        if len(palabras) == 0 or palabras[0] != "From":
            continue
        print(palabras[2])


# archivo = input("Introduzca el nombre del archivo: ")
buscar_dias()
