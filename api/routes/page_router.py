# routes/rag.py
from flask import Blueprint, jsonify, request

from api.page.page_dao import PageDAO
from api.connection.mysql_connection import get_db_connection
from api.reaction.reaction_manager import ReactionManager

page_bp = Blueprint('page', __name__, url_prefix='/api')
database = get_db_connection()
page_dao = PageDAO(database)
reaction_manager = ReactionManager(database)

@page_bp.route('/pages/<int:page_id>', methods=['GET'])
def get_page_by_id(page_id):
    page = page_dao.get_page_id(page_id)
    if page is None:
        return jsonify({"message": f"Page avec l'ID {page_id} non trouvée."}), 404
    return jsonify(page), 200

@page_bp.route('/page/react', methods=['POST'])
def react():
    if request.is_json:
        data = request.get_json()
        if not data or 'id_page' not in data or 'id_user' not in data:
            return jsonify({"error": "Les champs 'id_page' et 'id_user' sont requis."}), 400
        resp = reaction_manager.react(data['id_page'], data['id_user'])
        if resp:
            return jsonify({"message": "success"}), 200
        else:
            return jsonify({"error": "Erreur lors de la réaction."}), 500
    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400

@page_bp.route('/page', methods=['POST'])
def add_page():
    if request.is_json:
        data = request.get_json()
        if not data or 'content' not in data or 'components' not in data or 'status' not in data or 'emotion' not in data or 'id_user' not in data  or 'music_path' not in data or 'theme' not in data:
            return jsonify({"error": "Email and password are required."}), 400
        page_id = page_dao.addPage(data)
        if page_id is None:
            return jsonify({"error": "Invalid email or password."}), 401
        else:
            return jsonify({"page_id" :page_id}), 200
    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400


@page_bp.route('/pages', methods=['GET'])
def get_pages():
    pages = page_dao.get_page()
    if pages is None:
        return jsonify({"error": f"Erreur lors de la récupération des pages avec l'utilisateur "}), 500
    else:
        return jsonify({"pages": pages}), 200

# @page_bp.route('/register', methods=['POST'])
# def register():
#     if request.is_json:
#         data = request.get_json()
#         if not data or 'name' not in data or 'firstname' not in data or 'email' not in data or 'password' not in data:
#             return jsonify({"error": "Tous les champs (name, firstname, lastname, email, password) sont requis."}), 400
#         email = data['email']
#
#         if auth.check_email_exists(email):
#             return jsonify({"error": "Cet email est déjà enregistré."}), 409  # Conflict
#         user = auth.add_user(data)
#         if user:
#             return jsonify(user), 201  # Created
#         else:
#             return jsonify({"error": "L'inscription a échoué."}), 500
#
#
#     else:
#         return jsonify({'message': 'ataovy json lty eh'}), 400
# Ajoute d'autres routes RAG ici...