from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprints
    from .routes import bp as users_bp
    app.register_blueprint(users_bp)

    # Future: configs, db init, CLI, etc.
    return app
