import requests
from typing import Any, Dict

AWESOME_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
REQUEST_TIMEOUT = 5  # segundos


def get_usd_to_brl() -> Dict[str, Any]:
    """Busca a cotação atual USD->BRL na AwesomeAPI.

    Retorna um dicionário simplificado:
        {
          "pair": "USD-BRL",
          "bid": float,
          "timestamp": str | None
        }

    Levanta:
        ValueError: se a resposta não tiver o formato esperado.
        requests.RequestException: se houver erro de rede/HTTP.
    """
    resp = requests.get(AWESOME_URL, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()

    data = resp.json()
    usdbrl = data.get("USDBRL")
    if not usdbrl or "bid" not in usdbrl:
        raise ValueError("Resposta inválida da AwesomeAPI")

    return {
        "pair": "USD-BRL",
        "bid": float(usdbrl["bid"]),
        "timestamp": usdbrl.get("create_date"),
    }
