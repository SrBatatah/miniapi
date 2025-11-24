from flask import Blueprint, jsonify
from .services.exchange_service import get_usd_to_brl


exchange_bp = Blueprint("exchange", __name__, url_prefix="/exchange")


@exchange_bp.get("/usd-to-brl")
def usd_to_brl():
    """Retorna a cotação atual de USD para BRL via AwesomeAPI.

    Em caso de falha externa ou de formato inesperado, retorna 502
    com mensagem controlada, sem expor detalhes internos.
    """
    try:
        result = get_usd_to_brl()
        return jsonify(result), 200
    except ValueError:
        return jsonify({"error": "Resposta inválida da API de câmbio"}), 502
    except Exception:
        return jsonify({"error": "Falha ao consultar API de câmbio"}), 502
