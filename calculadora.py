# -*- coding: utf-8 -*-

from flask import Flask, request      #flask: paquete   .   Flask: clase, request: objeto

app = Flask(__name__)  #__name__  --> llamar como el archivo

@app.route("/")     #
def index():
    return "<h1 style='color:rgb(171, 173, 31)'>Calculadora</h1>"

@app.route("/Sumas")
def sumar():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    resultadoS = x + y
    return str(resultadoS)



if __name__ == "__main__":   #solo va a correr cuando se le llame directamente, no cuando sea importado.
    app.run(debug=True)
