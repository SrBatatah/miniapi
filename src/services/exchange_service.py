import requests

AWESOME_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

def get_usd_to_brl():
    """Busca cotação atual USD->BRL na AwesomeAPI.

    Retorna um dicionário simplificado com o par de moedas, o valor de compra (bid)
    e o timestamp retornado pela API.
    """
    resp = requests.get(AWESOME_URL, timeout=5)
    resp.raise_for_status()

    data = resp.json()
    usdbrl = data.get("USDBRL")
    if not usdbrl or "bid" not in usdbrl:
        raise ValueError("Resposta inválida da AwesomeAPI")

    return {
        "pair": "USD-BRL",
        "bid": float(usdbrl["bid"]),
        "timestamp": usdbrl.get("create_date")
    }
