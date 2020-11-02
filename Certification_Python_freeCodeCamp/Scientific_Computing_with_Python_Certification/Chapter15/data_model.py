# Vamos hacer un modelado de una base de datos
# ejemplo de una aplicacion de registro de canciones

# vamos a tener las siguientes columnas y tenedremos que
# decidir si estaran todas en la misma tabla o tablas distintas
# Nombre_cancion
# duracion
# album
# artista
# genero
# puntuacion
# numero de reproducciones

# Con estos datos podemos darnos cuenta que si los ponemos
# todos en la misma tabla inclumplimos uno de los fundamentos
# el de no repetir el mismo string, ya que tendríamos
# el mismo album, varias veces el mismo artista, el mismo
# genero

# decidimos que los nombres de las canciones tracks van a
# ser por lo que se va a buscar en la app, y entorno a
# ello vamos a relacionar las demás tablas

# los datos que son independientes para cada cancion son:
# su puntuacion duracion y reproducciones esas estarán
# en la misma tabla

# mientras que para evitar la duplicidad vertical en las
# columnas tendrán su propia tabla para el album,
# artista y genero

# Cada cancion pertenece a un genero
# Cada cancion pertenece a un album y cada album pertenece a un artista

# Tendremos 4 tablas
