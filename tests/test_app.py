from app.main import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200


def test_crear_cliente():
    client = app.test_client()

    response = client.post(
        "/api/clientes",
        json={
            "nombre": "Juan Perez",
            "email": "juan@test.com",
            "rfc": "ABCD123456EFG",
            "telefono": "5555555555"
        }
    )

    assert response.status_code == 201


def test_listar_clientes():
    client = app.test_client()

    response = client.get("/api/clientes")

    assert response.status_code == 200


def test_obtener_cliente():
    client = app.test_client()

    response = client.get("/api/clientes/1")

    assert response.status_code in [200, 404]


def test_rfc_invalido():
    client = app.test_client()

    response = client.post(
        "/api/clientes",
        json={
            "nombre": "Pedro",
            "email": "pedro@test.com",
            "rfc": "RFCMAL",
            "telefono": "5555555555"
        }
    )

    assert response.status_code == 400