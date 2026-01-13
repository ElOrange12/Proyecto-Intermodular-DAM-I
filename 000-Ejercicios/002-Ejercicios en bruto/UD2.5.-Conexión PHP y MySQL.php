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
