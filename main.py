from flask import Flask, Blueprint

from api.routes.auth_router import auth_bp
from api.routes.capsule_router import capsule_bp
from api.routes.emotion_router import emotion_bp
from api.routes.page_router import page_bp
from api.routes.refactor_router import refactor_bp
from api.routes.upload import upload_bp

app = Blueprint('main', __name__)

app.register_blueprint(emotion_bp)
app.register_blueprint(refactor_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(page_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(capsule_bp)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
