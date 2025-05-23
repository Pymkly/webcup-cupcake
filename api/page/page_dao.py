import json

from api.auth.auth_manager import AuthManager


class PageDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.auth = AuthManager(self.db_connection)

    def get_page_id(self, page_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
                SELECT
                    p.id AS page_id,
                    p.content,
                    p.components,
                    p.status,
                    p.emotion,
                    p.id_user,
                    u.name AS user_name,
                    u.firstname AS user_firstname,
                    COALESCE(prc.reaction_count, 0) AS reaction_count,
                    music_path,
                    theme
                FROM
                    page p
                JOIN
                    utilisateur u ON p.id_user = u.id
                LEFT JOIN
                    page_reaction_counts prc ON p.id = prc.id_page
                WHERE
                    p.id = %s;
                """
        cursor.execute(query, (page_id,))
        page_with_user = cursor.fetchone()
        cursor.close()
        if page_with_user is None:
            return None
        page_with_user['components'] = json.loads(page_with_user['components'])
        return page_with_user

    def get_page(self):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
            SELECT
            p.id AS page_id,
            p.content,
            p.status,
            p.emotion,
            p.id_user,
            u.name AS user_name,
            u.firstname AS user_firstname,
            COALESCE(prc.reaction_count, 0) AS reaction_count,
            music_path,
            theme
        FROM
            page p
        JOIN
            utilisateur u ON p.id_user = u.id
        LEFT JOIN
                    page_reaction_counts prc ON p.id = prc.id_page
        order by COALESCE(prc.reaction_count, 0) desc, p.id asc ;
        """
        cursor.execute(query)
        pages_with_user = cursor.fetchall()
        cursor.close()
        return pages_with_user

    def addPage(self, page):
        user = self.auth.get_user_by_id_db(page['id_user'])
        if user is None:
            return None
        _global_content = json.dumps(page['components'])
        cursor = self.db_connection.cursor()
        query = "INSERT INTO page (content, components, status, emotion, id_user, music_path, theme) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (page['content'], _global_content, page['status'], page['emotion'],  page['id_user'], page['music_path'], page['theme'])

        cursor.execute(query, values)
        self.db_connection.commit()
        page_id = cursor.lastrowid
        cursor.close()
        return page_id