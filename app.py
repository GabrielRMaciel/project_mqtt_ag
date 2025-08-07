from flask import Flask, jsonify, render_template
import sqlite3
from db import conectar, ler_dados


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dados")
def dados():
    data = ler_dados()
    return jsonify([
        {"timestamp": linha[0], "valor": linha[1]} for linha in data
    ])

if __name__ == "__main__":
    app.run(debug=True)

