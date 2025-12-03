from flask import Flask

aplicacion = Flask(__name__)
    
if __name__ == '__main__':
    aplicacion.run(debug=True)
