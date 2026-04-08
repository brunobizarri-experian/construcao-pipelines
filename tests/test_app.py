import pytest
from calculadora_web.app import create_app


# -------------------------------------------------------------------
# FIXTURES (configuração básica para todos os testes)
# -------------------------------------------------------------------

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


# -------------------------------------------------------------------
# ITEM 5 – Teste da rota GET "/"
# -------------------------------------------------------------------

def test_home_page_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Calculadora" in response.data


# -------------------------------------------------------------------
# ITEM 6 – Testes das operações (POST)
# -------------------------------------------------------------------

def test_soma(client):
    response = client.post(
        "/",
        data={
            "num1": "10",
            "num2": "5",
            "operacao": "soma",
        },
    )
    assert response.status_code == 200
    assert b"15" in response.data


def test_subtracao(client):
    response = client.post(
        "/",
        data={
            "num1": "10",
            "num2": "3",
            "operacao": "subtracao",
        },
    )
    assert b"7" in response.data


def test_multiplicacao(client):
    response = client.post(
        "/",
        data={
            "num1": "4",
            "num2": "5",
            "operacao": "multiplicacao",
        },
    )
    assert b"20" in response.data


def test_divisao(client):
    response = client.post(
        "/",
        data={
            "num1": "10",
            "num2": "2",
            "operacao": "divisao",
        },
    )
    assert b"5" in response.data


def test_divisao_por_zero(client):
    response = client.post(
        "/",
        data={
            "num1": "10",
            "num2": "0",
            "operacao": "divisao",
        },
    )
    assert b"Erro" in response.data