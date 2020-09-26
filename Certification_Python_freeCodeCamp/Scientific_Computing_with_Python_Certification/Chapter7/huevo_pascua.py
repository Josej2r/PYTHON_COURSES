nombre_archivo = input("Introduzca el nombre del archivo: ")
contador_lineas = 0

try:
    manejador_archivo = open(nombre_archivo)

    for lineas in manejador_archivo:
        contador_lineas += 1

    print(f"Hay {contador_lineas} lineas subject en {nombre_archivo}")
except:
    if nombre_archivo == "na na boo boo":
        print(" NA NA BOO BOO PARA TI - Te he atrapado!")
    else:
        print(f"El archivo no puede ser abierto: {nombre_archivo}")
