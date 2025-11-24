from unittest.mock import patch
from src.app import create_app


def test_usd_to_brl_route_success():
    app = create_app()
    client = app.test_client()

    fake_payload = {
        "pair": "USD-BRL",
        "bid": 5.0,
        "timestamp": "2025-11-23 12:00:00",
    }

    with patch("src.exchange_routes.get_usd_to_brl", return_value=fake_payload):
        resp = client.get("/exchange/usd-to-brl")

    assert resp.status_code == 200
    assert resp.get_json() == fake_payload


def test_usd_to_brl_route_invalid_payload_returns_502():
    app = create_app()
    client = app.test_client()

    with patch("src.exchange_routes.get_usd_to_brl", side_effect=ValueError("bad payload")):
        resp = client.get("/exchange/usd-to-brl")

    assert resp.status_code == 502
    assert resp.get_json()["error"] == "Resposta inválida da API de câmbio"


def test_usd_to_brl_route_generic_failure_returns_502():
    app = create_app()
    client = app.test_client()

    with patch("src.exchange_routes.get_usd_to_brl", side_effect=Exception("boom")):
        resp = client.get("/exchange/usd-to-brl")

    assert resp.status_code == 502
    assert resp.get_json()["error"] == "Falha ao consultar API de câmbio"
