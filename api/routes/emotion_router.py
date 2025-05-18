# routes/rag.py
from http.client import responses

from flask import Blueprint, jsonify, request

from api.agent.emotion_detector import EmotionDetector
from api.agent.video_decryptor import VideoDecryptor

emotion_bp = Blueprint('emotion', __name__, url_prefix='/api')

detector = EmotionDetector()
video_decryptor = VideoDecryptor()

@emotion_bp.route('/emotion-detector', methods=['POST'])
def emotion_endpoint():
    if request.is_json:
        data = request.get_json()
        if data and 'text' in data:
            received_text = data['text']
            _emotions = detector.answer(received_text)
            print(f"Texte reçu en JSON: {received_text}")
            return jsonify({"emotions": _emotions}), 200
    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400

@emotion_bp.route('/emotion-detector-urls', methods=['POST'])
def emotion_endpoint_urls():
    if request.is_json:
        data = request.get_json()
        if data and 'urls' in data:
            urls = data['urls']
            _responses = video_decryptor.detect_from_urls(urls)
            print(_responses)
            return jsonify(_responses), 200
    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400
# Ajoute d'autres routes RAG ici...