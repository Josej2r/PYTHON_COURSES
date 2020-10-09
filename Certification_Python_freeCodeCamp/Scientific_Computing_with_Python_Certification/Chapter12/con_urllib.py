import urllib.request, urllib.parse, urllib.error

URL = input("Introduzcca la URL :")
# http://data.pr4e.org/romeo.txt
try:
    fhand = urllib.request.urlopen(URL)
except:
    print("La URL introducidad no es correcta: ")
    exit()
for linea in fhand:
    print(linea.decode().split())
