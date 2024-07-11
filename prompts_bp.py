import psycopg2
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from authentification_bp import role_required
from db_conn import get_db_connection
from querry import transform_data_to_json, all_selected_prompts, get_prompt_owner

prompts_bp = Blueprint('prompts', __name__)

db = get_db_connection('promptprojectdb')
curs = db.cursor()


@prompts_bp.route('/create', methods=['POST'])
@jwt_required()
@role_required('user')
def create_prompt():
    content = request.json.get('content')

    user_info = get_jwt_identity()
    username_user = user_info.get('username')
    # print(username_user)

    if content:
        curs.execute("""INSERT INTO prompts (prompt_content, user_info) VALUES (%s, %s)""", (content, username_user))
        db.commit()
        db.close()
        return jsonify(msg='Prompt succesfuly create')
    else:
        return jsonify(msg='Missing values')


# Code pour supprimer un prompt
@prompts_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete(id):
    try:
        # id = request.json.get('id')
        curs.execute("""DELETE FROM prompts WHERE id = %s""", (id,))
        db.commit()
        # db.close()
        return jsonify(msg='Prompt Sucessfuly deleted')
    except (psycopg2.Error, Exception) as e:
        return jsonify(msg=f'Error: {e}')


# route pour activer un prompt
@prompts_bp.route('/activate/<int:id_prompt>', methods=['PUT'])
@jwt_required()
@role_required('admin')
def validate(id_prompt):
    try:
        # id = request.json.get('id')
        curs.execute("""UPDATE prompts SET status = 'active' WHERE id = %s""", (id_prompt,))
        db.commit()
        # db.close()
        return jsonify(msg='Prompt Successfully activated')
    except (psycopg2.Error, Exception) as e:
        return jsonify(msg=f'Error: {e}')


# Route pour demander la suppression de son propre prompt
@prompts_bp.route('/ask-to-delete/<int:id_prompt>', methods=['PUT'])
@jwt_required()
@role_required('user')
def prompt_asked_to_delete(id_prompt):
    user_info = get_jwt_identity()
    username = user_info.get('username')

    try:
        if username == get_prompt_owner(id_prompt):
            curs.execute("""UPDATE prompts SET status = 'delete' WHERE id = %s""", (id_prompt,))
            db.commit()
            # db.close()
            return jsonify(msg='Prompt Successfully added to to deleted prompt')
        else:
            return jsonify(msg="Sorry You can't delete this prompt. You're not the prompt owner ")
    except Exception as e:
        return jsonify(msg=f'Error : {e}')


# Route pour voter sur unn prompt afin de l'activer ou

# Route pour afficher tous les prompts
@prompts_bp.route('/dashboard', methods=['GET'])
@jwt_required()
@role_required('admin')
def list_prompts():
    json_data = [
        {
            'content': item[0],
            'owner': item[1],
            'price': item[2],
            'status': item[4]
        } for item in all_selected_prompts]
    return jsonify(json_data)
