# importing required libraries
import mysql.connector

def get_db_connection():
    try:
        db_connection = mysql.connector.connect(
            host="102.18.113.78",
            user="cupcake_root",
            passwd="passADMIN321?",
            database="cupcake_base"
        )
        return db_connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None