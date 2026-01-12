En este ejercicio se combinan conceptos de desarrollo web tanto del lado del cliente como del lado del servidor. Por un lado, se trabaja con JavaScript y la Fetch API para leer información desde un archivo JSON en el navegador. Por otro, se utiliza Flask para crear un microservidor que permite servir una página HTML y sus recursos asociados.

El objetivo principal es comprender cómo se puede cargar información estructurada en formato JSON y mostrarla dinámicamente en una página web, utilizando un servidor ligero en Python. Este tipo de arquitectura es muy común en aplicaciones web modernas, donde el servidor entrega la página y el cliente se encarga de consumir y mostrar los datos.

---

El ejercicio se divide en varias partes claramente diferenciadas. En primer lugar, se crea un microservidor utilizando Flask. Para ello, se importa la librería necesaria y se inicializa una nueva aplicación:

```
	from flask import Flask, render_template

	app = Flask(__name__)
```

A continuación, se define una ruta raíz mediante el decorador `@app.route('/')`. Esta ruta se ejecutará cuando el usuario acceda a la dirección principal del servidor. Dentro de la función asociada, se renderiza una plantilla HTML llamada `index.html`:

```
	@app.route('/')
	def inicio():
		return render_template("index.html")
```

Finalmente, se comprueba si el archivo se está ejecutando como programa principal. En ese caso, se arranca el servidor en modo depuración, lo que facilita la detección de errores durante el desarrollo:

```
	if __name__ == '__main__':
		app.run(debug = True)
```

Una vez el microservidor está en funcionamiento, Flask se encarga de servir la plantilla HTML. En el archivo `index.html`, se define la estructura básica de la página y se incluyen elementos HTML que actuarán como contenedores de la información que se cargará desde el archivo JSON.

Dentro del documento HTML se utiliza JavaScript junto con la Fetch API para realizar una petición GET a un archivo JSON situado en la carpeta `static`. La función `fetch()` solicita el archivo y, tras recibir la respuesta, se convierte a formato JSON:

```
	fetch('static/informacion.json')
	.then(function(respuesta){
		return respuesta.json();    
	})
```

Una vez obtenidos los datos, se muestran por consola para comprobar su contenido y, posteriormente, se utilizan para reemplazar el texto de los elementos HTML mediante el DOM:

```
	.then(function(datos){
		console.log(datos);         
		document.querySelector("h1").textContent = datos.nombre
		document.querySelector("h2").textContent = datos.forma
		document.querySelector("h3").textContent = datos.caras
	})
```

De esta forma, los valores almacenados en el archivo JSON se cargan dinámicamente en la página web sin necesidad de recargarla.

El archivo JSON contiene información estructurada relacionada con un cubo de Rubik, utilizando pares clave–valor que facilitan el acceso a los datos desde JavaScript.

---

_Microservidor.py_

```
	from flask import Flask, render_template

	app = Flask(__name__)

	@app.route('/')
	def inicio():
		# Y renderizo una plantilla llamada index.html
		return render_template("index.html")

	if __name__ == '__main__':
		app.run(debug = True)
```

_template/index.html_

```
	<!DOCTYPE html>
	<html lang="es">
		<head>
		    <title>Cubos de Rubik</title>
		    <meta charset="utf-8">
		</head>
		<body>
		    <h1>--nombre--</h1>
		    <h2>--forma--</h2>
		    <h3>--caras--</h3>
		    <script>
		        fetch('static/informacion.json')
		        .then(function(respuesta){
		            return respuesta.json();    
		        })
		        .then(function(datos){
		            console.log(datos);         
		            document.querySelector("h1").textContent = datos.nombre
		            document.querySelector("h2").textContent = datos.forma
		            document.querySelector("h3").textContent = datos.caras
		        })
		    </script>
		</body>
	</html>
```

_static/informacion.json_

```
	{
		"nombre":"Megaminx",
		"forma":"Dodecaédrica",
		"caras":"12"
	}
```

**Notas:**
- Se utiliza Flask para crear un microservidor web en Python.
- La ruta raíz renderiza una plantilla HTML.
- El navegador carga datos JSON mediante Fetch API.
- El contenido del JSON se procesa y se muestra dinámicamente en la página.
- Se trabaja con archivos estáticos para separar datos y presentación.

---

Este ejercicio permite comprender cómo interactúan el servidor y el cliente en una aplicación web sencilla. A través del uso de Flask, se aprende a servir páginas HTML, mientras que con Fetch API se practica la lectura y manipulación de datos JSON en el navegador. Esta combinación de tecnologías sienta las bases para desarrollar aplicaciones web más dinámicas y estructuradas, facilitando la gestión de información y su presentación al usuario.
