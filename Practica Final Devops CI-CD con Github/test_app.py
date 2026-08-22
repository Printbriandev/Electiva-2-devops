import pytest

from app import MENSAJE, crear_app


@pytest.fixture
def cliente():
    app = crear_app()
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente


def test_la_raiz_responde_200(cliente):
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200


def test_la_raiz_devuelve_el_mensaje_hola_mundo(cliente):
    respuesta = cliente.get("/")
    assert respuesta.get_data(as_text=True) == MENSAJE
    assert "Hola Mundo" in respuesta.get_data(as_text=True)


def test_salud_devuelve_json_con_estado_ok(cliente):
    respuesta = cliente.get("/salud")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"estado": "ok", "mensaje": MENSAJE}


def test_una_ruta_inexistente_devuelve_404(cliente):
    respuesta = cliente.get("/no-existe")
    assert respuesta.status_code == 404
