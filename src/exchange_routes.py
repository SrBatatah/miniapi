from flask import Blueprint, jsonify
from .services.exchange_service import get_usd_to_brl

exchange_bp = Blueprint("exchange", __name__, url_prefix="/exchange")

@exchange_bp.get("/usd-to-brl")
def usd_to_brl():
    """Endpoint que retorna a cotação atual USD->BRL."""
    try:
        result = get_usd_to_brl()
        return jsonify(result), 200
    except Exception as e:
        # Em caso de erro na API externa ou parsing, retornamos Bad Gateway
        return jsonify({"error": str(e)}), 502
