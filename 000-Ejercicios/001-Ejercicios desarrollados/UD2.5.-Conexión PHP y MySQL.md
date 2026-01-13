En este ejercicio se trabaja la creación de un blog dinámico utilizando PHP y MySQL. El objetivo es aprender a conectar una aplicación web con una base de datos, ejecutar consultas SQL y mostrar los resultados en una página HTML con una estructura clara y un estilo visual definido mediante CSS.

Este tipo de práctica es muy común en el desarrollo web, ya que combina backend (PHP y MySQL) con frontend (HTML y CSS), permitiendo mostrar contenido almacenado en una base de datos de forma dinámica y ordenada, simulando el funcionamiento real de un blog.

---

El archivo comienza con un comentario de cabecera donde se describe el nombre del proyecto, la versión y la finalidad del mismo. Este bloque sirve como documentación general del ejercicio.

A continuación, se define la estructura HTML básica del documento. Dentro de la etiqueta `<head>` se incluye una sección `<style>` donde se establecen los estilos CSS que darán forma visual al blog:

```
	<style>
	  body,html{
		font-family:monospace;
	  }
	  header,main,footer{
		width:800px;
		margin:auto;
		padding:20px;
	  }
	  p{
		text-align:justify;
	  }
	  article{
		border-bottom:1px solid grey;
	  }
	  header,footer{
		text-align:center;
	  }
	</style>
```

Estos estilos permiten centrar el contenido, mejorar la legibilidad del texto y separar visualmente cada artículo del blog.

Dentro del cuerpo del documento (`<body>`), se estructuran tres secciones principales: `header`, `main` y `footer`. En la cabecera se muestra el título del blog y el nombre del autor.

En la sección `<main>` se inserta el código PHP encargado de gestionar la conexión a la base de datos y la obtención de los artículos. En primer lugar, se definen las variables necesarias para conectarse al servidor MySQL:

```
	$host = "localhost";
	$user = "blogphp";
	$pass = "Blog123$";
	$db   = "blogphp";
```

Con estos datos, se crea una nueva conexión utilizando la clase `mysqli`:

```
	$conexion = new mysqli($host, $user, $pass, $db);
```

Una vez establecida la conexión, se define una consulta SQL que selecciona todos los registros de la tabla `blog`:

```
	$sql = "SELECT * FROM blog";
```

La consulta se ejecuta y se almacena el resultado en una variable:

```
	$resultado = $conexion->query($sql);
```

A continuación, se utiliza un bucle `while` junto con el método `fetch_assoc()` para recorrer cada uno de los registros obtenidos. Cada fila se recibe en forma de array asociativo, lo que permite acceder a los campos mediante el nombre de la columna:

```
	while ($fila = $resultado->fetch_assoc()) {
```

Dentro del bucle, se imprime el contenido de cada artículo utilizando etiquetas HTML semánticas como `<article>`, `<h3>`, `<time>` y `<p>`, dando forma estructurada a cada entrada del blog:

```
	echo '
	  <article>
		<h3>'.$fila['titulo'].'</h3>
		<time>'.$fila['fecha_publicacion'].'</time>
		<p>'.$fila['contenido'].'</p>
	  </article>
	';
```

Finalmente, una vez mostrados todos los artículos, se cierra la conexión con la base de datos para liberar recursos:

```
	$conexion->close();
```

---

```
	<!--
		Blog superinteresante
		v1.0 Daniel Oliveira Vidal
		Un blog que muestra en una página unos articulos sacando el contenido de una base de datos
	-->

	<!doctype html>
	<html>
		<head>
	  	<style>
			body,html{
		  	font-family:monospace;
		  }
		  header,main,footer{
		    width:800px;
		    margin:auto;
		    padding:20px;
		  }
		  p{
		  	text-align:justify;
		  }
		  article{
		  	border-bottom:1px solid grey;
		  }
		  header,footer{
		  	text-align:center;
		  }
		</style>
	  </head>
	  <body>
	  	<header>
			<h1>Daniel Oliveira Vidal</h1>
		  <h2>Blog superinteresante</h2>
		</header>
		<main>
		  <?php

		    $host = "localhost";
		    $user = "blogphp";
		    $pass = "Blog123$";
		    $db   = "blogphp";

		    $conexion = new mysqli($host, $user, $pass, $db);

		    $sql = "SELECT * FROM blog";

		    $resultado = $conexion->query($sql);

		    while ($fila = $resultado->fetch_assoc()) {
		      echo '
		        <article>
		          <h3>'.$fila['titulo'].'</h3>
		          <time>'.$fila['fecha_publicacion'].'</time>
		          <p>'.$fila['contenido'].'</p>
		        </article>
		      ';
		    }

		    $conexion->close();

		  ?>
	  	</main>
	  	<footer>
	  	</footer>
	  </body>
	</html>
```

**Notas:**
- Se realiza una conexión a una base de datos MySQL desde PHP.
- Se ejecuta una consulta SQL para obtener los artículos del blog.
- Los resultados se recorren mediante un bucle `while`.
- Cada artículo se muestra utilizando etiquetas HTML semánticas.
- Se aplican estilos CSS para mejorar la presentación visual del contenido.

---

Este ejercicio permite comprender cómo PHP puede interactuar con una base de datos MySQL para construir páginas web dinámicas. A través de la ejecución de consultas SQL y la generación de contenido HTML, se simula el funcionamiento real de un blog. Además, el uso de estilos CSS ayuda a mejorar la apariencia final de la página, reforzando la importancia de separar contenido, lógica y presentación en el desarrollo web.
