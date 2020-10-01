archivo = input("Introduzca el archivo a leer: ")
manejador_archivo = open(archivo)
lista_definitiva = []

for linea in manejador_archivo:  # vamos pasando línea a línea
    lista = linea.split()
    print(lista)

    if lista_definitiva == []:
        lista_definitiva = lista
        print(f"Cuando esta vacia y compiamos la primera linea: {lista_definitiva}")
        continue

    for i in range(len(lista)):

        if(lista[i] not in lista_definitiva):
            lista_definitiva.append(lista[i])

lista_definitiva.sort()
print(f"Lista lista definitiva fuera del bucle: {lista_definitiva}")
