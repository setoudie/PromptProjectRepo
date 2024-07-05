from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from db_conn import get_db_connection
from querry import allUsers, allUserNames_list

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/register', methods=['POST'])
def register():
    #Recuperation des informations du json d'inscription
    firstname = request.json.get('firstname')
    group_id = request.json.get('group_id')
    id = request.json.get('id')
    lastname = request.json.get('lastname')
    password = request.json.get('password')
    username = request.json.get('username')

    falsely_list = ['None', 'null', ''] #List of non authorized username and password

    if username in falsely_list or password in falsely_list:
        return jsonify({'msg': 'Missing values'})
    elif username in allUserNames_list:
        return jsonify({'msg': f'User : {username} Already Exist'})
    elif username not in falsely_list and password not in falsely_list: # incomplete checking reste verif sur others information
        hashed_password = generate_password_hash(password=password)
        db = get_db_connection('promptprojectdb')
        curs = db.cursor()
        curs.execute("""INSERT INTO users (id, username, firstname, lastname, password, group_id)
                            VALUES (%s, %s, %s, %s, %s, %s) """, (id, username, firstname, lastname, hashed_password, group_id))
        db.commit()
        db.close()
        return jsonify({"msg": "User registered successfully"})
    else:
        return jsonify({'msg': 'c\'est quoi le probleme'})

@admin_bp.route('/users')
def manage_users():
    return "Gestion des utilisateurs"


@admin_bp.route('/all-users')
def user_list():
    columns = ['id', 'username', 'firstname', 'lastname', 'password', 'group_id']
    users = [dict(zip(columns, user)) for user in allUsers]
    return jsonify(users)
