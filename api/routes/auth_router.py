# routes/rag.py
from flask import Blueprint, jsonify, request

from api.auth.auth_manager import AuthManager
from api.connection.mysql_connection import get_db_connection

auth_bp = Blueprint('auth', __name__, url_prefix='/api')
database = get_db_connection()
auth = AuthManager(database)

@auth_bp.route('/login', methods=['POST'])
def login():
    if request.is_json:
        data = request.get_json()
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({"error": "Email and password are required."}), 400
        email = data['email']
        password = data['password']
        user = auth.authenticate(email, password)
        if user is None:
            return jsonify({"error": "Invalid email or password."}), 401
        else:
            return jsonify(user), 200
    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400

@auth_bp.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
        if not data or 'name' not in data or 'firstname' not in data or 'email' not in data or 'password' not in data:
            return jsonify({"error": "Tous les champs (name, firstname, lastname, email, password) sont requis."}), 400
        email = data['email']

        if auth.check_email_exists(email):
            return jsonify({"error": "Cet email est déjà enregistré."}), 409  # Conflict
        user = auth.add_user(data)
        if user:
            return jsonify(user), 201  # Created
        else:
            return jsonify({"error": "L'inscription a échoué."}), 500


    else:
        return jsonify({'message': 'ataovy json lty eh'}), 400
# Ajoute d'autres routes RAG ici...