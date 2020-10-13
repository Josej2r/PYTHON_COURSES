import sqlite3

conn = sqlite3.connect('direcciones.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS users')
cur.execute('CREATE TABLE users (name VARCHAR(128), email VARCHAR(128))')

# Para inserta elementos a la tabla
# cur.execute('INSERT INTO users (name, email) VALUES ( 'Krisn', 'kf@umich.edu')')
cur.execute('INSERT INTO users (name, email) VALUES ( ?, ?)', ('Pepe', 'ppe@umich.edy'))

conn.commit()
