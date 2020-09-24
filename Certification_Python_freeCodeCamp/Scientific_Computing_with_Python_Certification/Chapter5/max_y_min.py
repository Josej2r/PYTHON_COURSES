maximo = None
minimo = None

while True:
    str_entrada = input("Intoduce un número: ")

    if str_entrada == "fin":
        break
    try:
        float_entrada = float(str_entrada)   # si introduce un str que no sea fin dara error y pasara al except
    except:
        print("Entrada inválida")
        continue

    if maximo is None and minimo is None:
        maximo = float_entrada
        minimo = float_entrada
    elif maximo < float_entrada:
        maximo = float_entrada
    elif minimo > float_entrada:
        minimo = float_entrada

print(f"El máximo es: {maximo}")
print(f"El mínimo es: {minimo}")
