archivo = input("Introduzca el nombre del archivo: ")
manejador_archivo = open(archivo)
contador = 0
for linea in manejador_archivo:
    palabras = linea.split()
    if len(palabras) == 0 or palabras[0] != "From":
        continue
    contador += 1
    print(palabras[1])
print(f"Hay {contador} lineas en el archivo que empiezan con la palabra From al inicio")
