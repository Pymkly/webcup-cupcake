# routes/rag.py
from flask import Blueprint, jsonify, request

from api.capsule.capsule_manager import CapsuleManager
from api.connection.mysql_connection import get_db_connection

capsule_bp = Blueprint('capsule', __name__, url_prefix='/api')
database = get_db_connection()
capsule_manager = CapsuleManager(database)

@capsule_bp.route('/capsules/<int:id_capsule>/checkpass', methods=['POST'])
def check_capsule_passphrase(id_capsule):
    if request.is_json:
        password = request.get_json().get('password')
        state = capsule_manager.check_pass(id_capsule, password)
        return jsonify({'state': state})
    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400

@capsule_bp.route('/users/<int:id_user>/capsules/<int:id_capsule>/available', methods=['GET'])
def is_capsule_available(id_user, id_capsule):
    state = capsule_manager.is_capsule_available(id_capsule, id_user)
    return jsonify({'state': state})

@capsule_bp.route('/users/<int:id_user>/capsules', methods=['GET'])
def get_user_capsules(id_user):
    capsules = capsule_manager.get_user_capsules(id_user)
    return jsonify(capsules)

@capsule_bp.route('/capsule/<int:id_capsule>', methods=['GET'])
def get_capsule_by_id(id_capsule):
    capsules = capsule_manager.get_capsule_by_id_w_pass(id_capsule)
    return jsonify(capsules)
@capsule_bp.route('/capsule', methods=['POST'])
def add_capsule():
    if request.is_json:
        data = request.get_json()
        if not data or 'title' not in data or 'elements' not in data or 'idUser' not in data:
            return jsonify({"error": "Les champs 'title', 'elements' et 'idUser' sont requis."}), 400
        capsule_id = capsule_manager.insert_capsule_db(data)
        if not capsule_id:
            return jsonify({"error": "Erreur lors de l'insertion de la capsule."}), 500
        for element in data['elements']:
            if 'ordre' not in element or 'title' not in element or 'type' not in element or 'idUser' not in element:
                database.rollback()
                return jsonify(
                    {"error": "Chaque élément de la capsule doit avoir 'order', 'title', 'type' et 'idUser'."}), 400
            if not capsule_manager.insert_capsule_element_db(element, capsule_id):
                database.rollback()
                return jsonify({"error": "Erreur lors de l'insertion d'un élément de la capsule."}), 500
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400


# Ajoute d'autres routes RAG ici...