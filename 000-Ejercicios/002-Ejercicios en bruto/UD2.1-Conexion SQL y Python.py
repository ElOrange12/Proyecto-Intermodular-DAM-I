'''
	Conexión base de datos
	v1.0 Daniel Oliveira Vidal
	Este programa conecta con una base de datos y devuelve la información en forma de diccionario
'''

import mysql.connector 

conexion = mysql.connector.connect(
  host='localhost',
  user='Tienda',
  password='Contraseña123$',
  database='Tienda'
)                                      
  
cursor = conexion.cursor(dictionary=True) 
cursor.execute('''
  SELECT
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
  FROM clientes
  ORDER BY edad DESC;
''')  

filas = cursor.fetchall()

print(filas)
