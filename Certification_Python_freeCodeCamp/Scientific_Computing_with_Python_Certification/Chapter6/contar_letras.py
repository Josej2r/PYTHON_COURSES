def cuenta(palabra, busco):
    contador = 0

    for cada_letra in palabra:
        if cada_letra is busco:
            contador += 1
    return contador


palabra = input("Introduzca la palabra: ")
letra = input("Introduzca la letra que quiere buscar")
contador = cuenta(palabra, letra)
print(f"La letra {letra} se encuentra en la palabra '{palabra}' , {contador} veces")
