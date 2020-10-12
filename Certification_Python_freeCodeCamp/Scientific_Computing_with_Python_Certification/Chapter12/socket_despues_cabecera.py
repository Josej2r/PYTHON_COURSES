# solamente mostraremos los datos después de recibir la cabecera y la línea
# en blanco

import socket
import time

URL = input("Introduzca la URL :")
# http://data.pr4e.org/romeo.txt


misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
contador_caracteres = 0
almacen_texto = b''
try:
    host = URL.split('/')
    host = host[2]
    puerto = 80

    misock.connect((host, puerto))
except:
    print('Dirrecion introducida erronea')
    exit()

cmd = "GET " + URL + " HTTP/1.0\r\n\r\n"
cmd = cmd.encode()
print(cmd)
misock.send(cmd)

while True:
    datos = misock.recv(1)
    if len(datos) < 1:
        break
    # time.sleep(0.25)
    contador_caracteres = contador_caracteres + len(datos)
    # vamos contando el número de caracteres recibidos en cada solicitud,
    # podemos indicar los que pedimos en recv()
    # print(f" Los caracteres recibidos {len(datos)} el total {contador_caracteres}")
    # el print anterior para ver la cantidad de caracteres recibidos y acumulados

    almacen_texto = almacen_texto + datos
    if datos == b"\r\n":
        print(datos.decode(), end='')
        # print("lo hemos encontado")

    else:

        continue


misock.close()
