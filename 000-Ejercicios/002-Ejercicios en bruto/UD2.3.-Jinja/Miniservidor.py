from flask import Flask, render_template
import mysql.connector

## MySQL

conexion = mysql.connector.connect(
	host='localhost',
	user='creadorportafolio',
	password='PortafolioExamen2526$',
	database='portafolioexamen'
)

cursor = conexion.cursor()		
cursor.execute('SHOW TABLES;')

tablas = []	

filas = cursor.fetchall()
for fila in filas:				
	tablas.append(fila[0])

## Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/clientes')
def clientes():
    return render_template("clientes.html")
    
@app.route('/productos')
def productos():
    return render_template("productos.html")

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

if __name__ == '__main__':
    app.run(debug = True)