import sqlite3

conn = sqlite3.connect('direcciones.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS users')
cur.execute('CREATE TABLE users (name VARCHAR(128), email VARCHAR(128))')

# Para inserta elementos a la tabla
# TENER EN CUENTA QUE NO PODEMOS PONER EL MISMO TIPO DE COMILLAS ''  ""

# cur.execute("INSERT INTO users (name, email) VALUES ( 'Krisn', 'kf@umich.edu')")
cur.execute('INSERT INTO users (name, email) VALUES ( ?, ?)', ('Kristin', 'kf@umich.edu'))
cur.execute('INSERT INTO users (name, email) VALUES ( ?, ?)', ('Chuck', 'csev@umich.edu'))
cur.execute('INSERT INTO users (name, email) VALUES ( ?, ?)', ('Colleen', 'cvl@umich.edu'))
cur.execute('INSERT INTO users (name, email) VALUES ( ?, ?)', ('Ted', 'ted@umich.edu'))
cur.execute('INSERT INTO users (name, email) VALUES ( ?, ?)', ('Sally', 'a1@umich.edu'))

conn.commit()

# borar una columna en funcion de un criterio de seleccion
cur.execute('DELETE FROM users WHERE email="ted@umich.edu"')

conn.commit()

# Para cambiar el dato correspondiente a alguna comlumna usamos UPDATE

cur.execute("UPDATE users SET name ='Charles' WHERE email='csev@umich.edu'")

conn.commit()

# Para seleccinar todos los elementos o solamente algunos lo podemos hacer con
# SELECT tamabién podemos usar el WHERE para seleccinarlos con un criterio


# Seleccionamos todos los elementos
cur.execute("SELECT * FROM users")

for linea in cur:
    print(linea)

# Seleccionamos solamente los correspondiente al criterio indicado

cur.execute("SELECT * FROM users WHERE name ='Charles'")

print("La dirección de Charles es: ")

for nombre in cur:
    print(nombre)

# Ordenar los datos seleccionados usando ORDER BY

cur.execute(" SELECT * FROM users ORDER BY email")

print("\n Orden ascendete en funcion del Email")
for orden_asc in cur:
    print(orden_asc)

cur.execute(" SELECT * FROM users ORDER BY name DESC")

print("\n Orden descendete en función del nombre")
for orden_desc in cur:
    print(orden_desc)
