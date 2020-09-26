nombre_archivo = input("Introduzca el nombre del archivo: ")
manejador_archivo = open(nombre_archivo)
contador_lineas = 0
acumulado = 0
for linea in manejador_archivo:
    linea = linea.rstrip()

    if linea.startswith("X-DSPAM-Confidence:"):
        tam_linea = len(linea)
        pos_puntos = linea.find(":")
        valor_str = linea[pos_puntos + 1:]
        acumulado = acumulado + float(valor_str)
        contador_lineas += 1


print(f"Valor medio es: {acumulado/contador_lineas}")
