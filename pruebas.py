# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")     #
def index():
    return "<h1 style='color:rgb(181, 29, 29)'>Calculadora</h1>"


@app.route('/Sumas')
def sumar():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(resultado=a + b)


@app.route('/Restas')
def restar():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(resultado=a - b)


@app.route('/Multi')
def multi():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(resultado=a * b)


@app.route('/Divi')
def divi():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(resultado=a / b)

if __name__ == '__main__':
    app.run()
