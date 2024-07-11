from flask import request, jsonify
from flask_jwt_extended import jwt_required
from your_auth_module import role_required  # Assurez-vous d'importer votre propre décorateur role_required
import psycopg2
import psycopg2.extras


@prompts_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete(id):
    try:
        # Connexion à la base de données
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_user",
            password="your_db_password",
            host="your_db_host",
            port="your_db_port"
        )
        curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Exécution de la requête DELETE
        curs.execute("DELETE FROM prompts WHERE id = %s", (id,))

        # Commit des changements
        conn.commit()

        # Fermeture du curseur et de la connexion
        curs.close()
        conn.close()

        return jsonify({"message": "Prompt deleted successfully"}), 200
    except psycopg2.Error as e:
        # Gestion des erreurs de la base de données
        if conn:
            conn.rollback()
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
