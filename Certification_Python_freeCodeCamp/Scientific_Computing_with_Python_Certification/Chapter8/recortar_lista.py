def recortar(lista):
    print(f"La lista antes: {lista}")
    lista = lista[1:]
    print(f"La lista después {lista}")
    # sin embargo la lista_para_recortar sigue siendo igual


def medio(lista):
    lista = lista[1:]
    return lista


lista_para_recortar = ["a", "b", "c", "d", "e"]
recortar(lista_para_recortar)
print(lista_para_recortar)

centro = medio(lista_para_recortar)
print(lista_para_recortar)
print(centro)
