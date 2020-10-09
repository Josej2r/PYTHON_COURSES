import socket

URL = input("Introduzca la URL :")
# http://data.pr4e.org/romeo.txt


misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    host = URL.split('/')
    host = host[2]
    misock.connect((host, 80))
except:
    print('Dirrecion introducida erronea')
    exit()

cmd = "GET " + URL + " HTTP/1.0\r\n\r\n"
cmd = cmd.encode()
print(cmd)
misock.send(cmd)

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end='')

misock.close()
