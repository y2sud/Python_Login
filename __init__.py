from flask import Flask
from .model import Model

def create_app():
    app = Flask(__name__)
    app.secret_key = 'jkrgn,n,24352n54'

    from .main import main
    app.register_blueprint(main)

    return app