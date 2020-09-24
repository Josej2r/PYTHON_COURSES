suma = 0
cantidad_num = 0

while True:
    str_entrada = input("Intoduce un número: ")

    if str_entrada == "fin":
        break
    try:
        float_entrada = float(str_entrada)   # si introduce un str que no sea fin dara error y pasara al exept
    except:
        print("Entrada inválida")
        continue

# como tenemos primero el If de fin y luego el continue no llegamos al contador
# a menos que lo introducido sea un numero , y así en la media la division es
# solamente con los numeros introducidos
    cantidad_num = cantidad_num + 1
    suma = suma + float_entrada

print(f"La suma es: {suma}")
print(f"Cantidad de numeros introducidos es: {cantidad_num}")
print(f"La media es: {suma/cantidad_num}")
