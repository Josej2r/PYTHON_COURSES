import re

fname = input("Introduzca el nombre del archivo: ")
fhand = open(fname)

regExp = "^New Revision: ([0-9]+)"

lst_suma = list()

for linea in fhand:
    linea = linea.rstrip()
    x = re.findall(regExp, linea)
    if len(x) > 0:
        lst_suma.append(float(x[0]))


promedio = sum(lst_suma)/len(lst_suma)
print(f"El promedio es {promedio}")
