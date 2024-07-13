from datetime import timedelta
from functools import wraps
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, decode_token, jwt_required, get_jwt_identity, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash
from db_conn import get_db_connection
from querry import all_users_hashed_pass_list, all_users_usernames_list

auth_bp = Blueprint('auth', __name__)


# Creation de la route de connexion
@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # hash_password = request.json.get('password')

    conn = get_db_connection(db_name='promptprojectdb')
    cursor = conn.cursor()

    # Recherche de l'username dans la table admin
    cursor.execute('SELECT * FROM admins WHERE username = %s AND hashed_password = %s', (username, password))
    admin_info = cursor.fetchone()  # This is a tuple who contains all info about admin
    # admin_info --> ('username', 'firstname', 'lastname', 'not_hashed_password')

    if admin_info is not None:
        payload_data = {'username': admin_info[0], 'role': 'admin'}  # admin_info[0] --> username value
        access_token = create_access_token(identity=payload_data, expires_delta=timedelta(hours=3))
        conn.close()
        return jsonify({'access_token': access_token}), 200

    # Rechetrche de l'username dans la table users
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user_info = cursor.fetchone()  # This is a tuple of user's information it's like to :
    # ('username','firstname','lastname','hashed_password','group_id', 'admin_info')
    # print(admin_info)

    # Now we are checking that the input data (username and password ) are in our database
    print(user_info[-3])
    try:
        for pseudo, hash_pass in zip(all_users_usernames_list, all_users_hashed_pass_list):
            if pseudo == user_info[0] and check_password_hash(pwhash=user_info[-3], password=password):
                payload_data = {'username': user_info[0], 'role': 'user'}
                access_token = create_access_token(identity=payload_data, expires_delta=timedelta(hours=3))
                conn.close()
                return jsonify({'access_token': access_token}), 200
    except Exception as e:
        print(f"Type of erreur : {e}")
        return jsonify({'msg': 'Invalid credentials'}), 401

    conn.close()
    return jsonify({'msg': 'Invalid credentials'}), 401


# Fonction pour verifier le role de chaque personne
def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user_info = get_jwt_identity()  # getting payload data
            if user_info.get('role') != role:
                return jsonify({'msg': 'Error 403 Forbidden: Permission insuffisante'}), 403
            return fn(*args, **kwargs)

        return decorator

    return wrapper


@auth_bp.route('/logout')
def logout():
    return jsonify(msg='logout successfuly')
