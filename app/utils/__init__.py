from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import webhook_blueprint  # 👈 muévelo aquí
    app.register_blueprint(webhook_blueprint, url_prefix="/webhook")

    return app