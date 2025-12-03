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
