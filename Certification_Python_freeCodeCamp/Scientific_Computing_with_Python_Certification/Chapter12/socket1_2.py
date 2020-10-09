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
    datos = misock.recv(25)
    if len(datos) < 1:
        break
    time.sleep(0.25)
    contador_caracteres = contador_caracteres + len(datos)
    # vamos contando el número de caracteres recibidos en cada solicitud,
    # podemos indicar los que pedimos en recv()
    # print(f"Los caracteres recibidos {len(datos)} el total {contador_caracteres}")
    # el print anterior para ver la cantidad de caracteres recibidos y acumulados

    almacen_texto = almacen_texto + datos
    if contador_caracteres < 250:
        print(datos.decode(), end='')

    else:
        continue

# VERSION NO OPTIMA PERO HACE LO QUE SE PEDIA 
# Pero aqui fuera abriamos leido el texto entero y en len(almacen_texto)
# tendriamos todos los caracteres

print(f"\n La pagina tiene {len(almacen_texto)} caracteres")
# print(almacen_texto.decode(), end='')

misock.close()
