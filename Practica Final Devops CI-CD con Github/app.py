import os

from flask import Flask, jsonify

MENSAJE = "Hola Mundo - Practica Final DevOps CI/CD con GitHub"


def crear_app():
    app = Flask(__name__)

    @app.route("/")
    def hola_mundo():
        return MENSAJE

    @app.route("/salud")
    def salud():
        return jsonify({"estado": "ok", "mensaje": MENSAJE})

    return app


app = crear_app()


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
