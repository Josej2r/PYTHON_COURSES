import sqlite3

# Conectamos a la DB y sino existe la creamos
conn = sqlite3.connect('musica.sqlite')
cur = conn.cursor()  # El cursos es un manejador para poder hacer las operaciones

cur.execute('DROP TABLE IF EXISTS Canciones')  # Borramos si existe ya la tabla

# Creamos la tabla Canciones con dos columnas titulo y reproducciones indicamos
# el tipo de datos que almacenará
cur.execute('CREATE TABLE Canciones (titulo TEXT, reproducciones INTEGER)')

# Para insertar datos lo podemos hacer tal que así:

cur.execute(
    'INSERT INTO Canciones (titulo, reproducciones) VALUES (?, ?)', ('Mi carro', 50))
cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES (?, ?)',
            ('La macarena', 80))
cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES (?, ?)',
            ('La rosalía', 150))

# Esta forma de insertar datos me da error no se si es que no lo escribo bien
# cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES('My way', 15)')

# Linea importante para forzar que se guarden los datos en la DB

conn.commit()  # MUY IMPORTANTE ESTA LINEA PARA GUARDAR LOS DATOS

# Mostrar datos de la tabla

print("Canciones:")
# Seleccionamos las columnas de titulo y reproducciones de la tabla Canciones
cur.execute('SELECT titulo, reproducciones FROM Canciones')
for fila in cur:
    print(fila)

# Para eliminar alguna fila de la tabla

cur.execute('DELETE FROM Canciones WHERE reproducciones < 100')
conn.commit()  # para forzar a los datos que se eliminen de la DB


# Para comprobar que las canciones con menos de 100 repro se han borrado
print("Canciones:")
# Seleccionamos las columnas de titulo y reproducciones de la tabla Canciones
cur.execute('SELECT titulo, reproducciones FROM Canciones')
for fila in cur:
    print(fila)


cur.close()  # También importante el cerrar el manejador
