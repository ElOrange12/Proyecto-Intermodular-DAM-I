En este ejercicio se trabaja con la conexión a una base de datos MySQL utilizando Python. El objetivo principal es aprender a establecer una conexión correcta con una base de datos, realizar una consulta SQL seleccionando campos concretos y obtener los resultados en formato diccionario para facilitar su manejo posterior.

Este tipo de ejercicios es fundamental cuando se empieza a trabajar con bases de datos, ya que permite comprender cómo interactúan las aplicaciones con sistemas de almacenamiento de información externos y cómo se pueden recuperar los datos de forma estructurada y ordenada.

---

El programa comienza con un comentario de cabecera que identifica el ejercicio, la versión y una breve descripción de su funcionalidad. Esta información es útil para documentar el código y entender rápidamente su propósito.

A continuación, se importa el módulo `mysql.connector`, que es el encargado de permitir la comunicación entre Python y una base de datos MySQL:

```
	import mysql.connector
```

Seguidamente, se establece la conexión con la base de datos mediante el método `connect()`. En esta parte se indican los datos necesarios para acceder al servidor, como el host, el usuario, la contraseña y el nombre de la base de datos:

```
	conexion = mysql.connector.connect(
	  host='localhost',
	  user='Tienda',
	  password='Contraseña123$',
	  database='Tienda'
	)
``` 

Una vez creada la conexión, se obtiene un cursor a partir de ella. En este caso, el cursor se configura con el parámetro `dictionary=True`, lo que permite que los resultados de las consultas se devuelvan en forma de diccionario, usando los nombres de las columnas como claves:

```
	cursor = conexion.cursor(dictionary=True)
```

Posteriormente, se ejecuta una consulta SQL mediante el método `execute()`. La consulta selecciona los campos `nombre`, `apellidos` y `edad de la tabla `clientes`, asignando alias a cada campo para que los nombres sean más descriptivos en el resultado final. Además, se utiliza la cláusula `ORDER BY edad DESC` para ordenar los registros por edad de mayor a menor:

```
	cursor.execute('''
	  SELECT
	  nombre AS 'Nombre del cliente',
	  apellidos AS 'Apellidos del cliente',
	  edad AS 'Edad del cliente'
	  FROM clientes
	  ORDER BY edad DESC;
	''')
```

Una vez ejecutada la consulta, se recuperan todos los registros obtenidos utilizando el método `fetchall()`. Este método devuelve una lista con todos los resultados de la consulta, donde cada elemento corresponde a un registro de la base de datos:

```
	filas = cursor.fetchall()
```

Finalmente, se imprimen los resultados por pantalla. Al haberse utilizado un cursor en modo diccionario, cada fila se muestra como un diccionario, lo que facilita el acceso a los datos mediante claves:

```
	print(filas)
```

---

```
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
```

**Notas:**
- Se utiliza el módulo mysql.connector para conectarse a una base de datos MySQL.
- La conexión se configura mediante los parámetros de acceso al servidor.
- Se crea un cursor en modo diccionario para obtener los resultados de forma estructurada.
- Se ejecuta una consulta SQL con proyección de campos y ordenación.
- Los resultados se recuperan con fetchall() y se muestran por pantalla.

---

Este ejercicio permite afianzar los conceptos básicos de acceso a bases de datos desde Python, incluyendo la creación de conexiones, la ejecución de consultas SQL y la obtención de resultados en formato diccionario. El uso de este formato facilita el tratamiento de los datos y resulta especialmente útil en aplicaciones donde se requiere claridad y organización en la información recuperada. Estos conocimientos son la base para el desarrollo de aplicaciones más complejas que trabajan con bases de datos.
