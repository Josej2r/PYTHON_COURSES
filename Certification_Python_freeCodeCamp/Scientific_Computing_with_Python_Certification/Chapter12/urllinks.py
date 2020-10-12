import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca - ')
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')

# mostramos los enlaces que se encuentran en la pagina, no es la version depurada
'''
etiquetas = sopa('a')
for etiqueta in etiquetas:
    print(etiqueta.get('href', None))
'''

contador_parrafos = 0
etiquetas = sopa('p')
for etiqueta in etiquetas:
    contador_parrafos += 1

print(f"Hay {contador_parrafos} párrafos en esta página {url}")
