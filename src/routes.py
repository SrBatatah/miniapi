from flask import Blueprint, jsonify, request
from .models import USERS

bp = Blueprint("users", __name__)

@bp.route("/users", methods=["GET"])
def list_users():
    return jsonify(USERS), 200

@bp.route("/users", methods=["POST"])
def create_user():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    email = payload.get("email")
    if not name or not email:
        return {"error": "name and email are required"}, 400

    new_id = (max([u["id"] for u in USERS]) + 1) if USERS else 1
    USERS.append({"id": new_id, "name": name, "email": email})
    from flask import url_for
    resp = {"id": new_id}
    return resp, 201, {"Location": url_for("users.get_user", user_id=new_id)}

@bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    user = next((u for u in USERS if u["id"] == user_id), None)
    if not user:
        return {"error": "not found"}, 404
    return user, 200

@bp.route("/health", methods=["GET"])
def health():
    # readiness/liveness probe
    return {"status": "ok"}, 200
