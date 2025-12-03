Vamos a realizar el examen trimestral de proyecto en este uniremos las siguientes tres materias: Programación, Bases de Datos y Lenguajes de Marcas, utilizando la información almacenada en nuestra base de datos, el lenguaje `html` aprendido en clase y utilizaremos la librería `flask` en `python`.

Esto hará una aplicación de `python` la cual hosteé una página en `html` dinámica en base a nuestra base de datos.

---

Primero de todo importamos las librerías que vamos a utilizar en este caso son `mysql.connector` para enlazar con la base de datos y `flask` para hacer un host para nuestra pàgina:

```
	import mysql.connector                    
	from flask import Flask
```

Ahora empezemos dando las credenciales necesarias para poder entrar en la base de datos:

```
	conexion = mysql.connector.connect(
		host='localhost',
		user='creadorportafolio',
		password='PortafolioExamen2526$',
		database='portafolioexamen'
	)                                      
	cursor = conexion.cursor() 
```

Despues definimos la ruta de la página:

```
	@app.route("/") 
```

Ya con todo esto empezemos con la página, para ello definiremos una función:

```
	def contenidoVista(): 
```

Dentro de esta pediremos la información a mostrar en la base de datos y empezaremos una cadena en esta estará todo el contenido `html`, además de un bucle `for` en el apartado de main, este nos permitirá mostrar la información que hemos pedido a la base de datos, así lo haremos de una forma que se repita las veces iguales al contenido que haya:

```
	cursor.execute("SELECT * FROM vista_piezas;")  

	filas = cursor.fetchall()                 
	  
	cadena = ''' 
		<!doctype html>
			<html lang="es">
			    <head>
					<title>Portafolio</title>
					<meta charset="utf-8">
					<style>
					  html,body{background:BurlyWood;font-family:sans-serif;}
					  header,main,footer{
						background:FloralWhite;
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
					  main img{
						width: 100%; /* No quiero que la imagen se salga */ 
					  }
					  </style>
			  	</head>
			    <body>
					<header>
						<h1>Portafolio</h1>
						<h2>info@elorange.com</h2>
					</header>
					<main>
		  '''                               
		  for fila in filas:
			cadena += '''
						<article>
							<p>'''+fila[3]+'''</p>
							<h3>'''+fila[0]+'''</h3>
							<p>'''+fila[1]+'''</p>
							<p>'''+fila[2]+'''</p>
							<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
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

```
	import mysql.connector                    
	from flask import Flask                   

	conexion = mysql.connector.connect(
		host='localhost',
		user='creadorportafolio',
		password='PortafolioExamen2526$',
		database='portafolioexamen'
	)                                      
	cursor = conexion.cursor()                
	app = Flask(__name__)                     

	@app.route("/")                           
	def contenidoVista():                          
	  cursor.execute("SELECT * FROM vista_piezas;")  

	  filas = cursor.fetchall()                 
	  
	  cadena = ''' 
		<!doctype html>
			<html lang="es">
			  <head>
				<title>Portafolio</title>
				<meta charset="utf-8">
				<style>
				  html,body{background:BurlyWood;font-family:sans-serif;}
				  header,main,footer{
					background:FloralWhite;
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
				  main img{
					width: 100%; /* No quiero que la imagen se salga */ 
				  }
				</style>
			  </head>
			  <body>
				<header>
				  <h1>Portafolio</h1>
				  <h2>info@elorange.com</h2>
				</header>
				<main>
	  '''                               
	  for fila in filas:
		cadena += '''
				    <article>
						<p>'''+fila[3]+'''</p>
						<h3>'''+fila[0]+'''</h3>
						<p>'''+fila[1]+'''</p>
						<p>'''+fila[2]+'''</p>
						<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
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
```
**Notas:**

- A la hora de hacer un bucle `for` en base a una cadena saber que información guarda cada pasición en la cadena.
- Importante el uso de las tres "'" para abrir y cerrar el `DocString`.
- No olvidarse de poner ":" después de definir funciones, estructuras de selección y demás estructuras similares.

---

En conclusión hemos visto como conectar en un mismo programa los distintos programas que hicimos anteriormente, así podemos darnos cuenta de la compatibilidad entre los lenguajes que utilizamos y la importancía de utilizarlos juntos.

Esto nos hace ver como podemos hacer programas sencillos en una web, siendo dinámicos y a nuestro gusto.


