# routes/rag.py
import os
import time

from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_uploads import UploadSet, ALL


upload_bp = Blueprint('upload', __name__, url_prefix='/api')


@upload_bp.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' in request.files:
        video = request.files['video']
        timestamp = int(time.time())
        _filename = secure_filename(f"{timestamp}_{video.filename}")
        _path = os.path.join('static', _filename)
        video.save(_path)
        _url = f"/static/{_filename}"
        return jsonify({"message": "Vidéo uploadée avec succès.", "filename": video.filename, "url": _url}), 201
    else:
        return jsonify({"error": "Aucun fichier vidéo n'a été envoyé."}), 400
