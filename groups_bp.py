from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from authentification_bp import role_required
from db_conn import get_db_connection

groups_bp = Blueprint('groups', __name__)

LOC_DB_NAME = "promptprojectdb"
HEROKU_DB_NAME = "d3svebcrtcq9m"


# Route creation groupe d'users
@groups_bp.route('/create', methods=['POST'])
@jwt_required()
@role_required('admin')
def creat_group():
    group_name = request.json.get('group_name')

    admin_info = get_jwt_identity()
    username_info = admin_info.get('username')

    db = get_db_connection()
    curs = db.cursor()
    curs.execute("""INSERT INTO groups (group_name, admin_info) VALUES (%s, %s)""", (group_name, username_info))
    db.commit()
    db.close()
    return jsonify(msg='Group Creer')


@groups_bp.route('/list')
def list_groups():
    return "Liste des groupes"
