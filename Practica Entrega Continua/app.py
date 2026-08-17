import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hola_mundo():
    return "Hola Mundo - Practica Entrega Continua (DevOps)"


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
