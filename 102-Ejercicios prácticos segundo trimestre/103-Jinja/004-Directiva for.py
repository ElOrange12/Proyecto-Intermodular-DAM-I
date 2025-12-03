from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
	mis_frutas = ['Manzanas', 'Peras', 'Platanos', 'Fresas']
	return render_template("lista.html", frutas = mis_frutas)
    
if __name__ == '__main__':
    app.run(debug = True)
