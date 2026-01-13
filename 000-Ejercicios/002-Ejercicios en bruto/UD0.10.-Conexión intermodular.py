'''
Calendario Web Dinámico
v1.0 Daniel Oliveira Vidal
Aplicación web con Flask que genera un calendario anual dinámico utilizando la librería calendar.
'''

from flask import Flask
import calendar
import datetime

app = Flask(__name__)

@app.route("/")
def raiz():
    # Obtenemos el año actual del sistema
    anio = datetime.datetime.now().year
    
    # Instanciamos el calendario HTML, configurando el primer día de la semana (Lunes)
    cal = calendar.HTMLCalendar(calendar.MONDAY)
    
    # Empezamos a construir la cadena HTML en línea
    cadena = '''
    <!doctype html>
    <html lang="es">
        <head>
            <title>Calendario Dinámico</title>
            <meta charset="utf-8">
            <style>
                body{
                    font-family:sans-serif; 
                    background:AntiqueWhite; 
                    text-align:center;
                }
                h1{
                    color:darkorange;
                    text-transform: uppercase;
                }
                .contenedor{
                    display:flex;
                    flex-wrap:wrap;
                    justify-content:center;
                    gap:20px;
                    padding:20px;
                }
                /* Estilos para las tablas generadas por calendar */
                table{
                    background:white;
                    border:2px solid darkorange;
                    border-collapse:collapse;
                }
                th{
                    background:darkorange;
                    color:white;
                    padding:5px;
                }
                th.month{
                    font-size: 1.2em;
                    background:#FFC880;
                    color:black;
                }
                td{
                    padding:5px;
                    border:1px solid #ddd;
                    text-align:center;
                }
                .noday{
                    background:#f3f3f3;
                }
            </style>
        </head>
        <body>
            <h1>Calendario '''+str(anio)+'''</h1>
            <div class="contenedor">
    '''
    
    # Recorremos los 12 meses del año para generar su HTML
    for mes in range(1, 13):
        cadena += cal.formatmonth(anio, mes)
        
    # Cerramos las etiquetas HTML
    cadena += '''
            </div>
            <footer>
                (c) 2026 Daniel Oliveira Vidal
            </footer>
        </body>
    </html>
    '''
    
    return cadena

if __name__ == "__main__":
    app.run(debug=True)