from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def rai ():
    cadena = '''
    <!doctype html>
    <html>
        <head>
            <title></title>
            <style>
                h1{color:red;}
            </style>
        </head>
        <body>
            <h1>Esto es HTML a tope de power</h1>
        </body>
    </html>
    '''
    
    return cadena
    
if __name__ == '__main__':
    aplicacion.run(debug=True)
