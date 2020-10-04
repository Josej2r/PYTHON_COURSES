direcciones_correo = dict()

fname = input("Introduzca el nombre del archivo: ")

try:
    fhand = open(fname)
except:
    print("El archivo no se puede abrir", fname)
    exit()
for lineas in fhand:
    lineas = lineas.rstrip()

    if not lineas.startswith("From "):
        continue
    # ha este punto solamnte llegan las lineas que empiezan por From

    # Separamos las frases por palabras usando split()
    lineas = lineas.split(" ")
    correo = lineas[1]  # tomamos la direccion de correo
    direcciones_correo[correo] = direcciones_correo.get(correo, 0) + 1

    # Ahora tenemos un diccionarios con las direcciones de correo y el número
    # de correos que a mandado cada persona

t = list(direcciones_correo.items())
# Creamos la lista de tuplas, (email, contador)

# ahora creamos la lista de tuplas pero del tipo (contador, email)

lst_orden_inv = list()
for email, contador in t:
    lst_orden_inv.append((contador, email))

# Ahora ya podemos usar el método sort para ordenar por el primer elemento de
# la lista de tuplas que es el contador

lst_orden_inv.sort(reverse=True)

# ahora tenemos que mostar la dirrecion que tiene mas mensajes, que será la
# que esta en primera posicion, pero ¿ podría usar max o algo así?
# print(max(lst_orden_inv)) sí se podría usar pero no nos da el orden que quermos

# Cambiamos el orden de la lst_orden_inv

for contador, email in lst_orden_inv[:1]:  # seleccionamos solamente el primero
    print(email, contador)
