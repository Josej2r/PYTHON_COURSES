puntuacion = input("Introduzca la puntuación entre 0.0 y 1.0: ")
calificacion = ""
try:
    puntuacion = float(puntuacion)

    if puntuacion >= 0.0 and puntuacion <= 1.0:
        # Si ponemos los if de las notas en otro orden siempre se cumple que
        # puntuacion es mayor por ej que puntuacion es mayor que 0.6 si lo
        # ponemos primero siempre saldrá suficiente

        if puntuacion >= 0.9:
            calificacion = "Sobrealiente"
        elif puntuacion >= 0.8:
            calificacion = "Notable"
        elif puntuacion >= 0.7:
            calificacion = "Bien"
        elif puntuacion >= 0.6:
            calificacion = "Suficiente"
        elif puntuacion < 0.6:
            calificacion = "Insuficiente"

        print(calificacion)

    else:
        print("Puntuación incorrecta")

except:
    print("Puntuación incorrecta")
