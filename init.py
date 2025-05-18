from flask import Flask
from flask_cors import CORS

def create_app():
    _app = Flask(__name__)
    CORS(_app)
    from main import app
    _app.register_blueprint(app)

    return _app
