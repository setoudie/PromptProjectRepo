from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
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
        access_token = create_access_token(identity=payload_data)
        conn.close()
        return jsonify({'access_token': access_token}), 200

    # Rechetrche de l'username dans la table users
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user_info = cursor.fetchone()  # This is a tuple of user's information it's like to :
    # ('id','username','firstname','lastname','hashed_password','group_id')
    # print(admin_info)

    # Now we are checking that the input data (username and password ) are in our database
    try:
        for pseudo, hash_pass in zip(all_users_usernames_list, all_users_hashed_pass_list):
            if pseudo == user_info[1] and check_password_hash(pwhash=user_info[-2], password=password):
                payload_data = {'username': user_info[1], 'role': 'user'}
                access_token = create_access_token(identity=payload_data)
                conn.close()
                return jsonify({'access_token': access_token}), 200
    except Exception as e:
        print(f"Type of erreur : {e}")
        return jsonify({'msg': 'Invalid credentials'}), 401

    conn.close()
    return jsonify({'msg': 'Invalid credentials'}), 401


@auth_bp.route('/logout')
def logout():
    return "Page de déconnexion"
