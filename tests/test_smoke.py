from src.app import create_app


def test_app_factory_creates_flask_app():
    app = create_app()
    assert app is not None
    assert hasattr(app, "test_client")
