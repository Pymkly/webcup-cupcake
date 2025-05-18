# routes/rag.py
from flask import Blueprint, jsonify, request

from api.agent.refactor import Refactor

refactor_bp = Blueprint('refactor', __name__, url_prefix='/api')

refactor = Refactor()

@refactor_bp.route('/refactor', methods=['POST'])
def emotion_endpoint():
    if request.is_json:
        data = request.get_json()
        if data and 'text' in data:
            received_text = data['text']
            _text = refactor.answer(received_text)
            print(f"Texte reçu en JSON: {received_text}")
            return jsonify({"text": _text}), 200
    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400

# Ajoute d'autres routes RAG ici...