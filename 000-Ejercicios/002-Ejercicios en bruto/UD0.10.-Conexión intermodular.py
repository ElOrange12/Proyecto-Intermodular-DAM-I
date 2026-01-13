from flask import Flask             

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  suma = 4+3
  cadena =  '''
    <!doctype html>
    <html>
      <head>
        <title>Hola Python</title>
        <style>
          .mes{
            width:700px;
            display:grid;
            grid-template-columns:auto auto auto auto auto auto auto;
          }
          .dia{
            width:100px;
            height:100px;
            border:1px solid grey;
          }
        </style>
      </head>
      <body>
      '''
  for mes in range(1,13):
    cadena += '''
      <div class="mes">
        '''
        
    for dia in range(1,31):
      cadena += '<div class="dia">'+str(dia)+'</div>'
    
    cadena += '''
            </div>
            '''
  cadena += '''
      </body>
    </html>
    
  '''
  return cadena
  
if __name__ == "__main__":
  aplicacion.run(debug=True)
