from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprints
    from .routes import bp as users_bp
    app.register_blueprint(users_bp)

    from .exchange_routes import exchange_bp
    app.register_blueprint(exchange_bp)

    return app
