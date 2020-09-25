def recorrer(cadena):

    indice = len(cadena)-1
    while indice >= 0:
        print(cadena[indice])
        indice = indice - 1


palabra = input("Introduzca el nombre de una fruta: ")
recorrer(palabra)
