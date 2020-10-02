palabra = "dinosaurio"

diccionario = dict()

for cada_letra in palabra:
    if cada_letra not in diccionario:
        diccionario[cada_letra] = "primera"
        print(diccionario)
    else:
        diccionario[cada_letra] = diccionario[cada_letra] + 1
print (diccionario)
