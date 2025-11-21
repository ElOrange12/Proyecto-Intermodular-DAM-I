# Importo librería flask para crear webs
from flask import Flask, render_template

# Creo una nueva aplicación
app = Flask(__name__)

# Escucho en la ruta raiz
@app.route('/')
def inicio():
    # Y renderizo una plantilla llamada index.html
    return render_template("index.html")

# Si este archivo no es una librería y es el archivo principal
if __name__ == '__main__':
    app.run(debug = True)