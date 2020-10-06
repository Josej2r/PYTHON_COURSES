# Encontrar las coincidendias en un archivo que se le pasa
# Usando las expresion regular que se le pasa

import re
expresion = input("Introduzca la expresión regular: ")
fname = input("Introduzca el nombre del archivo: ")

fhand = open(fname)

contador_lineas = 0

for linea in fhand:
    linea = linea.rstrip()
    if re.search(expresion, linea):
        contador_lineas += 1

print(f"{fname} tiene {contador_lineas} líneas que coinciden con {expresion}")
