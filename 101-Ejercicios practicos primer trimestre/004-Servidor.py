from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route('/')
def raiz():
#################### Esto es un bloque ####################
	cadena = ''' 
	<!doctype html>
<html lang="es">
	<head>
		<title>ElOrangeBLOG</title>
		<meta charset="utf-8">
		<style>
			body{background:steelblue; color:steelblue; font-family:sans-serif;}
			header, main, footer{background:white; padding:20px; margin:auto; width:600px;}
			header, footer{text-align:center;}
			main{color:black;}
		</style>
	</head>
	<body>
		<header><h1>ElOrangeBLOG</h1></header>
		<main>
		'''
		
#################### Esto es otro bloque ####################
	archivo = open('blog.json','r')
	contenido = json.load(archivo)
	
	for linea in contenido:
		cadena += '''
			<article>
				<h3>'''+linea['titulo']+'''</h3>
				<time>'''+linea['fecha']+'''</time>
				<p>'''+linea['autor']+'''</p>
				<p>'''+linea['contenido']+'''</p>
			</article>
			'''

#################### Esto es otro bloque ####################
	cadena += '''
		</main>
		<footer>(c)2025 Daniel Oliveira Vidal</footer>
	</body>
</html>
'''

#################### No os olvideis del return ####################
	return cadena

if __name__ == '__main__':
	aplicacion.run(debug = True)

for linea in contenido:
	print('###### ARTICULO ######')
	print(linea['titulo'])
	print(linea['fecha'])
	print(linea['autor'])
	print(linea['contenido'])
	print('######################')
	print('')
