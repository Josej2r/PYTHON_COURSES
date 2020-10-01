lista_almacen = []

while True:
    numero = input("Introduzca un número: ")
    if numero == "fin":
        break
    lista_almacen.append(numero)

print(f"El máximo es: {float(max(lista_almacen))}")
print(f"El mínimo es: {float(min(lista_almacen))}")
