import mysql


class AuthManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_user(self, user):
        cursor = self.db_connection.cursor()
        query = "INSERT INTO utilisateur (name, firstname, email, password) VALUES (%s, %s, %s, %s)"
        values = (user['name'], user['firstname'], user['email'], user['password'])  # **IMPORTANT: Hacher le mot de passe en production!**
        try:
            cursor.execute(query, values)
            self.db_connection.commit()
            user = self.get_user_from_db(user["email"])
            user['password'] = None
            cursor.close()
            return user
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
            self.db_connection.rollback()
            cursor.close()
            return None

    def check_email_exists(self, email):
        """Vérifie si un email existe déjà dans la base de données."""
        cursor = self.db_connection.cursor()
        query = "SELECT id FROM utilisateur WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def authenticate(self, email, password):
        user = self.get_user_from_db(email)
        print(user)
        if user and user['password'] == password :
            user['password'] = None
            return user
        return None

    def get_user_from_db(self, email):
        """Retrieves user data from the database based on email."""
        cursor = self.db_connection.cursor(dictionary=True)  # Fetch results as dictionaries
        query = "SELECT id, name, firstname, email, password FROM utilisateur WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def get_user_by_id_db(self, _id):
        """Retrieves user data from the database based on email."""
        cursor = self.db_connection.cursor(dictionary=True)  # Fetch results as dictionaries
        query = "SELECT id, name, firstname, email, password FROM utilisateur WHERE id = %s"
        cursor.execute(query, (_id,))
        user = cursor.fetchone()
        cursor.close()
        return user
