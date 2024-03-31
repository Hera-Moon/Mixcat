from flask import Flask


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> None:
    from .hello_api import hello_bp

    apis = [hello_bp]

    for api in apis:
        app.register_blueprint(api)
