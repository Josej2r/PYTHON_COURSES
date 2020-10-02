archivo = input("Introduzca el nombre del archivo: ")
manejador_archivo = open(archivo)

cadena_texto = manejador_archivo.read()  # todo como una cadena muy larga
cadena_texto = cadena_texto.rstrip()  # Eliminamos salto de linea
cadena_texto = cadena_texto.split()  # separamos por palabras

diccionario = dict()  # creamos un diccionario vacio

# ahora usamos un bucle para ir recorriendo todas las palabras y guardarlas,
# como claves del diccionario

for i in range((len(cadena_texto))):
    diccionario[cadena_texto[i]] = "pepe"

if "t" in diccionario:
    print("Lo encontre")
