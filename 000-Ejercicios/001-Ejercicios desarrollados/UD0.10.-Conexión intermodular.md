En este ejercicio se desarrolla una **aplicación web dinámica utilizando Flask**, cuyo objetivo es mostrar un **calendario completo del año actual** generado automáticamente desde Python. Para ello, se emplea la librería estándar `calendar`, que permite crear calendarios en distintos formatos, incluido HTML.

Este tipo de ejercicio es especialmente útil para comprender cómo Python puede generar contenido HTML de forma dinámica y servirlo directamente a través de un microservidor web, sin necesidad de plantillas externas. Además, se trabaja con fechas reales del sistema, lo que hace que la aplicación esté siempre actualizada.

---

El programa comienza con un comentario de cabecera donde se describe el propósito de la aplicación, su versión y su autor. Esto ayuda a documentar correctamente el proyecto.

A continuación, se importan las librerías necesarias:

```
    from flask import Flask
    import calendar
    import datetime
```

- `Flask` se utiliza para crear la aplicación web.

- `calendar` permite generar calendarios en distintos formatos.

- `datetime` se emplea para obtener el año actual del sistema.

Después, se crea la aplicación Flask:

```
    app = Flask(__name__)
```

Este objeto será el encargado de gestionar las rutas y el servidor web.

Se define la ruta raíz `(/)`, que será la página principal de la aplicación:

```
    @app.route("/")
    def raiz():
```

Dentro de esta función, lo primero que se hace es obtener el año actual:

```
    anio = datetime.datetime.now().year
```

Esto permite que el calendario sea dinámico, ya que se adaptará automáticamente al año en curso sin necesidad de modificar el código manualmente.

A continuación, se instancia un calendario HTML indicando que la semana debe comenzar en lunes:

```
    cal = calendar.HTMLCalendar(calendar.MONDAY)
```

La clase `HTMLCalendar` genera directamente tablas HTML, lo que facilita enormemente la creación del calendario visual.

Seguidamente, se comienza a construir una cadena de texto que contiene todo el documento HTML. Este HTML se genera en línea desde Python, incluyendo estructura, estilos CSS y contenido:

```
    cadena = '''
    <!doctype html>
    <html lang="es">
        <head>
            <title>Calendario Dinámico</title>
            ...
```

Dentro del bloque `<style>`, se definen los estilos del calendario, ajustando colores, tipografía y distribución. Se utilizan estilos para:

- El cuerpo de la página
- El título principal
- El contenedor de los calendarios
- Las tablas generadas automáticamente por `calendar`

Para generar el calendario completo del año, se recorre un bucle del 1 al 12, correspondiente a los meses del año:

```
    for mes in range(1, 13):
    cadena += cal.formatmonth(anio, mes)
```

Cada llamada a `formatmonth()` devuelve una tabla HTML con el calendario del mes correspondiente, que se va concatenando a la cadena principal.

Finalmente, se cierran las etiquetas HTML abiertas y se devuelve la cadena completa como respuesta del servidor:

```
    return cadena
```

De esta forma, Flask envía al navegador una página HTML completamente generada desde Python.

El programa finaliza iniciando el servidor en modo depuración:

```
    if __name__ == "__main__":
        app.run(debug=True)
```

Esto permite ver errores en tiempo real y facilita el desarrollo durante la práctica.

```
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
        
        for mes in range(1, 13):
            cadena += cal.formatmonth(anio, mes)
            
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
```

**Notas:**

- Se utiliza Flask como microframework web.
- El calendario se genera dinámicamente con la librería `calendar`.
- El año se obtiene automáticamente del sistema.
- El HTML se construye íntegramente desde Python.
- Se muestran los 12 meses del año en una sola vista.

---

Este ejercicio demuestra cómo es posible generar contenido HTML dinámico directamente desde Python utilizando Flask. El uso de la librería `calendar` facilita la creación de calendarios completos sin necesidad de escribir manualmente el HTML de cada mes. Además, al obtener el año actual del sistema, la aplicación se mantiene siempre actualizada, convirtiéndose en un ejemplo claro de aplicación web dinámica y funcional.