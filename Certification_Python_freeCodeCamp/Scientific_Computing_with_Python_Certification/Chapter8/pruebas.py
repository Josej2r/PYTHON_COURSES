cadena1 = "hola1 don1 pepito1 hola1 don1 jose"
cadena2 = "jose paso usted por su casa por su casa yo pase"

lista1 = cadena1.split()
lista2 = cadena2.split()
lista_definitiva = lista1
print(lista_definitiva)

for i in range(len(lista2)):
    if(lista2[i] not in lista_definitiva):
        lista_definitiva.append((lista2[i]))

lista_definitiva.sort()
print(lista_definitiva)
