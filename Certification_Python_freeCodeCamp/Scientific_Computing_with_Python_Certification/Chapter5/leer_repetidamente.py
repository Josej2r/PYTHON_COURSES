suma = 0
cantidad_num = 0

while True:
    str_entrada = input("Intoduce un número: ")

    if str_entrada == "fin":
        break
    try:
        float_entrada = float(str_entrada)
    except:
        print("Entrada inválida")
        continue

    cantidad_num = cantidad_num + 1
    suma = suma + float_entrada

print(f"La suma es: {suma}")
print(f"Cantidad de numeros introducidos es: {cantidad_num}")
print(f"La media es: {suma/cantidad_num}")
