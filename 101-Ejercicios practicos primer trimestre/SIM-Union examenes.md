En esta actividad se integran los conocimientos adquiridos en los exámenes de Bases de Datos, Programación y Lenguajes de Marcas.
  
Partiendo de la base de datos creada previamente, del código Python usado en programación y de la plantilla HTML/CSS diseñada en lenguajes de marcas, se construye una aplicación completa utilizando `Python` + `Flask`.
  
El objetivo principal es conectar la aplicación con MySQL mediante mysql.connector obtener los datos de la vista `piezas_y_categorias` y mostrarlos dinámicamente en la interfaz web, combinando así backend, frontend y base de datos en un único proyecto funcional.

---

Primero de todo importamos las librerías que vamos a utilizar en este caso son `mysql.connector` para enlazar con la base de datos y `flask` para hacer un host para nuestra pàgina:

```
	import mysql.connector                    
	from flask import Flask
```

Ahora empezemos dando las credenciales necesarias para poder entrar en la base de datos:

```
	conexion = mysql.connector.connect(
		host="localhost",
		user="portafolioceac",
		password="portafolioceac",
		database="portafolioceac"
	)                                       
	cursor = conexion.cursor()  
```

Despues definimos la ruta de la página:

```
	@app.route("/") 
```

Ya con todo esto empezemos con la página, para ello definiremos una función:

```
	def holamundo():
```

Dentro de esta pediremos la información a mostrar en la base de datos y empezaremos una cadena en esta estará todo el contenido `html`, además de un bucle `for` en el apartado de main, este nos permitirá mostrar la información que hemos pedido a la base de datos, así lo haremos de una forma que se repita las veces iguales al contenido que haya:

```
	cursor.execute("SELECT * FROM piezas_y_categorias;")  # Pido el contenido de la vista

	filas = cursor.fetchall()               
	cadena = ''' 
	<!doctype html>
	<html lang="es">
		<head>
			<title>Examen</title>
			<meta charset="utf-8">
			<style>
				html,body{background:grey;font-family:sans-serif;}
				header,main,footer{
					background:white;
					padding:20px;
					width:800px;
					margin:auto;
					text-align:center;
				}
				main{
					display:grid;
					grid-template-columns:auto auto auto;
					gap:20px;
				}
			</style>
		</head>
		<body>
			<header>
				<h1>Daniel Oliveira Vidal</h1>
				<h2>info@elorange12.com</h2>
			</header>
			<main>
			  '''                              
	for fila in filas:                        
	cadena += '''
				<article>
					<p>'''+fila[0]+'''</p>
					<h3>'''+fila[2]+'''</h3>
					<p>'''+fila[3]+'''</p>
					<img src="'''+fila[4]+'''">
				</article>
		'''
	cadena += ''' 
			</main>
			<footer>
	  			(c) 2025 Daniel Oliveira Vidal
			</footer>
		</body>
	</html>
	'''
```

Y por ultimo en la función pondremos un `return` que devuelva esta cadena.

Para acabar utilizamos una estructura de control que en el caso de sea la pagina principal ejecute la web:

```
	if __name__ == "__main__":                
		app.run(debug=True)
```


---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

'''
	import mysql.connector                  
	from flask import Flask                  

	conexion = mysql.connector.connect(
	  host="localhost",
	  user="portafolioceac",
	  password="portafolioceac",
	  database="portafolioceac"
	)                                     
	cursor = conexion.cursor()               
	app = Flask(__name__)                    
	@app.route("/")                          
	def holamundo():                          
		cursor.execute("SELECT * FROM piezas_y_categorias;")  # Pido el contenido de la vista

		filas = cursor.fetchall()               
		cadena = ''' 
		<!doctype html>
		<html lang="es">
			<head>
				<title>Examen</title>
				<meta charset="utf-8">
				<style>
					html,body{background:grey;font-family:sans-serif;}
					header,main,footer{
						background:white;
						padding:20px;
						width:800px;
						margin:auto;
						text-align:center;
					}
					main{
						display:grid;
						grid-template-columns:auto auto auto;
						gap:20px;
					}
				</style>
			</head>
			<body>
				<header>
					<h1>Daniel Oliveira Vidal</h1>
					<h2>info@elorange12.com</h2>
				</header>
				<main>
				  '''                              
		for fila in filas:                        
		cadena += '''
					<article>
						<p>'''+fila[0]+'''</p>
						<h3>'''+fila[2]+'''</h3>
						<p>'''+fila[3]+'''</p>
						<img src="'''+fila[4]+'''">
					</article>
			'''
		cadena += ''' 
				</main>
				<footer>
		  			(c) 2025 Daniel Oliveira Vidal
				</footer>
			</body>
		</html>
	  '''
	  return cadena                           

	if __name__ == "__main__":              
		app.run(debug=True)                  
'''

**Notas:**

- A la hora de hacer un bucle `for` en base a una cadena saber que información guarda cada pasición en la cadena.
- Importante el uso de las tres "'" para abrir y cerrar el `DocString`.
- No olvidarse de poner ":" después de definir funciones, estructuras de selección y demás estructuras similares.

---

Este ejercicio permite comprobar cómo diferentes áreas del desarrollo web pueden integrarse en un mismo proyecto.

Gracias a Flask se genera una página que mezcla partes estáticas —como la cabecera y el pie— con contenido dinámico obtenido desde la base de datos mediante un bucle que recorre los resultados de la vista.

El resultado final demuestra la capacidad de unir estructura HTML, lógica en Python y datos provenientes de MySQL para crear una aplicación web completa, organizada y totalmente funcional.
