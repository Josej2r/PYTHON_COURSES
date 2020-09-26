str = "X-DSPAM-Confidence : 0.8475"

pos_puntos = str.find(":")
print(pos_puntos)
str_num = str[pos_puntos +1 :]
print(str_num)
str_float = float(str_num)
print(type(str_float))
