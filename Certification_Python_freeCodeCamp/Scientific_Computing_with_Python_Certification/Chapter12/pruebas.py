# tenemos una cadena de texto
# cadena = " banana "
cadena = " Esto es una cadena de texto con espacios al final y principio    "
print(f"{cadena} del tipo {type(cadena)}")

sin_blank_spaces = cadena.strip()
print(f"{sin_blank_spaces} del tipo {type(sin_blank_spaces)}")

palabras = sin_blank_spaces.split()
print(f"{palabras} del tipo {type(palabras)}")


for palabra in palabras:
    for letra in palabra:
        print(letra)
