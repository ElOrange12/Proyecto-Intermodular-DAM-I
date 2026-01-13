En este ejercicio se trabaja con Flask para comprender cómo un servidor web puede recibir información enviada desde el navegador. A lo largo de la práctica, se utilizan parámetros en la URL y formularios HTML para enviar datos al servidor y procesarlos mediante Python.

El objetivo principal es entender el flujo de comunicación entre el cliente y el servidor, viendo cómo Flask puede recoger datos introducidos por el usuario y utilizarlos dentro del programa. Este tipo de funcionamiento es básico en el desarrollo de aplicaciones web dinámicas y formularios interactivos.

---

El programa comienza importando las librerías necesarias para trabajar con Flask, renderizar plantillas HTML y acceder a los datos enviados desde el navegador:

```
	from flask import Flask, render_template, request
```

A continuación, se crea una nueva aplicación Flask. Esta aplicación será la encargada de gestionar las peticiones HTTP que lleguen al servidor:

```
	pp = Flask(__name__)
```

Seguidamente, se define una ruta raíz utilizando el decorador `@app.route('/')`. Esta ruta se ejecuta cuando el usuario accede a la dirección principal del servidor y devuelve una plantilla HTML llamada `index.html`:

```
	@app.route('/')
	def inicio():
		return render_template('index.html')
```

Esta plantilla suele contener un formulario desde el cual el usuario puede enviar información al servidor.

Posteriormente, se define una segunda ruta llamada `/envio`. Esta ruta se encarga de recibir los datos enviados desde el navegador a través de la URL. Para ello, se utiliza el objeto `request` y el método `args.get()` para recuperar los valores asociados a los parámetros `nombre` y `apellidos`:

```
	nombre = request.args.get('nombre')
	apellidos = request.args.get('apellidos')
```

Estos valores corresponden a los datos introducidos por el usuario en el formulario o pasados directamente en la URL. Una vez recogidos, se imprimen en la consola del servidor para comprobar que han sido recibidos correctamente:

```
	print(nombre, apellidos)
```

Finalmente, el servidor devuelve una respuesta en forma de texto plano, mostrando los datos recibidos concatenados en una cadena:

```
	return 'nombre: '+nombre+' - apellidos: '+apellidos
```

Por último, se comprueba si el archivo se está ejecutando como programa principal. En ese caso, se inicia el servidor Flask en modo depuración, lo que facilita la visualización de errores durante el desarrollo:

```
	if __name__ == '__main__':
		app.run(debug = True)
```

---

```
	from flask import Flask, render_template, request

	app = Flask(__name__)

	@app.route('/')
	def inicio():
		return render_template('index.html')

	@app.route('/envio')
	def envio():
		nombre = request.args.get('nombre')
		apellidos = request.args.get('apellidos')
		print(nombre, apellidos)
		return 'nombre: '+nombre+' - apellidos: '+apellidos

	if __name__ == '__main__':
		app.run(debug = True)
```

**Notas:**

- Se crea un servidor web básico utilizando Flask.
- Se define una ruta raíz que renderiza una plantilla HTML.
- Se recogen parámetros enviados desde la URL mediante `request.args`.
- Los datos recibidos se muestran en la consola del servidor.
- El servidor devuelve una respuesta dinámica al navegador.

---

Este ejercicio permite comprender cómo Flask gestiona la recepción de datos enviados desde el navegador, tanto mediante parámetros en la URL como a través de formularios. Aprender a capturar y procesar esta información es esencial para el desarrollo de aplicaciones web interactivas, ya que sienta las bases para trabajar con formularios, validaciones y comunicación cliente-servidor en proyectos más avanzados.
