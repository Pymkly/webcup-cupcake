import mysql


class ReactionManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def react(self, id_page, id_user):
        if self.has_reacted(id_page, id_user):
            return self.remove_reaction(id_page, id_user)
        else:
            return self.add_reaction(id_page, id_user)

    def has_reacted(self, id_page, id_user):
        """Vérifie si un utilisateur a déjà réagi à une page."""
        cursor = self.db_connection.cursor()
        query = "SELECT id FROM reaction WHERE id_page = %s AND id_user = %s"
        cursor.execute(query, (id_page, id_user))
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def remove_reaction(self, id_page, id_user):
        """Supprime la réaction d'un utilisateur à une page."""
        cursor = self.db_connection.cursor()
        query = "DELETE FROM reaction WHERE id_page = %s AND id_user = %s"
        try:
            cursor.execute(query, (id_page, id_user))
            self.db_connection.commit()
            cursor.close()
            return cursor.rowcount > 0  # Retourne True si une ligne a été supprimée
        except mysql.connector.Error as e:
            print(f"Erreur lors de la suppression de la réaction : {e}")
            self.db_connection.rollback()
            cursor.close()
            return False

    def add_reaction(self, id_page, id_user):
        """Ajoute une réaction à une page."""
        cursor = self.db_connection.cursor()
        query = "INSERT INTO reaction (id_page, id_user) VALUES (%s, %s)"
        try:
            cursor.execute(query, (id_page, id_user))
            self.db_connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'ajout de la réaction : {e}")
            self.db_connection.rollback()
            cursor.close()
            return False