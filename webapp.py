# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
#flask: paquete   .   Flask: clase, request: objeto , render_template: objeto

app = Flask(__name__)  #__name__  --> llamar como el archivo

@app.route("/")     #
def index():
    return "<h1 style='color:rgb(171, 173, 31)'>Mi primera página web</h1>"


@app.route("/about")
def about():
    return "<h1 style='color:rgb(55, 31, 173)'>About Us</h1>"


@app.route("/contac")
def contact():
    return "<h1 style='color:rgb(31, 132, 173)'>Contact Us</h1>"


@app.route("/buy")
def buy():
    return "<h1 style='color:rgb(34, 157, 27)'>Buy</h1>"


@app.route("/saludar")
def saludar():
    name = request.args.get("name", "Fulano")     #http://localhost:500/saludar?name=Sebastian
    if not name:
        return "No hay a quien saludar"
    return "Hola " + name


@app.route("/echo")
def echo():
    reponse_string = u"Recibí: "     #<--- la "u" significa que tiene que convertir en unicode la cadena
    params = request.args
    for k, v in params.iteritems():
        reponse_string = reponse_string + ("%s: %s," % (k, v))

    return reponse_string


@app.route("/home")
def home():
    return render_template("home.html", appName="WIX", nombre="Sebasti")  #render_template utiliza jinja 2


@app.route("/Bio")
def bio():
    # return render_template("bio.html", nombreDePersona="Sebasti Garmen", edadDePersona="20", escuelaDePersona="Tec de Monterrey", trabajoDepersona="Prntex3D" )
    params = {
        "nombreDePersona": u"Sebastián",
        "edadDePersona": "20",
        "escuelaDePersona": "Tec de Monterrey",
        "trabajoDepersona": "Printex3D"
    }
    return render_template("bio.html", **params)


@app.route("/list")
def lista():
    lista = [
    {"nombre": "Ximena", "apodo": "Jimmy"},
    {"nombre": "Antonio", "apodo": u"Patrón"},
    {"nombre": u"Julián", "apodo": "Julaian"}
    ]
    return render_template("lista.html", lista=lista, title="Lista de grupo")


@app.route("/alumno/<ids>")
def getByApodo(ids):
    lista = {
        'ximena': {"nombre": "Ximena Ortega", "bio": "Alumna DevF" },
        'tono': {"nombre": "Antonio Banderas", "bio": "Le dicen el Patroncito"},
        'pablo': {"nombre": u"Pablo Velázquez", "bio": "Colorear"}
        }
    alumno = alumno.get(id)
    return render_template("alumno.html", lista=lista, title="Alumno")








if __name__ == "__main__":   #solo va a correr cuando se le llame directamente, no cuando sea importado.
    app.run(debug=True)
