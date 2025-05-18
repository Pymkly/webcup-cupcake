from flask import Flask
from flask_uploads import UploadSet, ALL, configure_uploads

from api.routes.emotion_router import emotion_bp
from api.routes.refactor_router import refactor_bp
from api.routes.auth_router import auth_bp
from api.routes.page_router import page_bp
from api.routes.capsule_router import capsule_bp
from flask_cors import CORS

from api.routes.upload import upload_bp

app = Flask(__name__)

CORS(app)

# app.config['UPLOADED_VIDEOS_DEST'] = 'static/videos'
# app.config['UPLOADED_VIDEOS_URL'] = '/static/videos/'

# videos = UploadSet('videos', ALL)
#
# configure_uploads(app, videos)

app.register_blueprint(emotion_bp)
app.register_blueprint(refactor_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(page_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(capsule_bp)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)