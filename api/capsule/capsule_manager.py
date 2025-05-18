import json
from datetime import datetime

import mysql


class CapsuleManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def check_pass(self, capsule_id, password):
        capsule = self.get_capsule_by_id(capsule_id)
        return capsule['passphrase'] == password


    def is_capsule_available(self, capsule_id, user_id):
        capsule = self.get_capsule_by_id(capsule_id)
        is_owner = capsule['id_user'] == user_id
        disponible_at = capsule['disponible_at']
        now = datetime.now()
        if is_owner and (disponible_at is None or now >= disponible_at):
            return True
        return False

    def get_capsule_by_id(self, capsule_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = "SELECT id, title, description, disponible_at, created_at, updated_at, music_url, emotions, id_user, passphrase FROM capsule WHERE id = %s"
        cursor.execute(query, (capsule_id,))
        capsule = cursor.fetchone()
        cursor.close()
        return capsule

    def get_capsule_by_id_w_pass(self, capsule_id):
        capsule = self.get_capsule_by_id(capsule_id)
        if capsule is None:
            return None
        capsule['passphrase'] = None
        return capsule


    def get_user_capsules(self, id_user):
        cursor = self.db_connection.cursor(dictionary=True)
        query = "SELECT id, title, description, disponible_at, created_at, updated_at, music_url, emotions, id_user FROM capsule WHERE id_user = %s"
        cursor.execute(query, (id_user,))
        capsules = cursor.fetchall()
        cursor.close()

        # Supprimer l'attribut 'passphrase' de chaque capsule
        for capsule in capsules:
            if 'passphrase' in capsule:
                del capsule['passphrase']

        return capsules


    def insert_capsule_element_db(self, element_data, capsule_id):
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO capsule_element (id_capsule, ordre, title, description, media_link, music_link, type, subtype, id_user)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            capsule_id,
            element_data['ordre'],
            element_data['title'],
            element_data['description'],
            element_data['mediaLink'],
            element_data['musicLink'],
            element_data['type'],
            element_data['subtype'],
            element_data['idUser']
        )
        try:
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            self.db_connection.rollback()
            cursor.close()
            return False

    def insert_capsule_db(self, capsule_data):
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO capsule (title, description, has_pass, passphrase, disponible_at, music_url, emotions, id_user)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            capsule_data['title'],
            capsule_data['description'],
            capsule_data['hasPass'],
            capsule_data['pass'],
            capsule_data['disponibleAt'],
            capsule_data['musicUrl'],
            json.dumps(capsule_data['emotions']),
            capsule_data['idUser']
        )
        try:
            cursor.execute(query, values)
            self.db_connection.commit()
            capsule_id = cursor.lastrowid
            cursor.close()
            return capsule_id
        except mysql.connector.Error as e:
            print(e)
            self.db_connection.rollback()
            cursor.close()
            return None

