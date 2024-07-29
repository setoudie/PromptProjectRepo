from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from db_conn import get_db_connection
from authentification_bp import role_required
from querry import all_users_data, all_users_usernames_list, all_admins_usernames_list, all_admins_hashed_pass_list

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/all-users')
def user_list():
    columns = ['id', 'username', 'firstname', 'lastname', 'password', 'group_id']
    users = [dict(zip(columns, user)) for user in all_users_data]
    return jsonify(users)
