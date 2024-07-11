import psycopg2
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from authentification_bp import role_required
from db_conn import get_db_connection
from querry import transform_data_to_json, all_selected_prompts, get_prompt_owner, get_user_group_id, get_prompt_price, \
    get_prompt_note, get_prompt_status, isInSameGroup, verif_activation

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
        # db.close()
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


# Route pour voter sur unn prompt afin de l'activer
@prompts_bp.route('/vote-for-activation/<int:id_prompt>', methods=['PUT', 'GET'])
@jwt_required()
@role_required('user')
def vote_for_activation(id_prompt):
    VOTING_WEIGHT = 1
    # curs = db.cursor()
    try:
        initial_prompt_note = get_prompt_note(id_prompt)
    except TypeError:
        return jsonify(msg=f"Not prompt with id = {id_prompt}")

    actual_prompt_status = get_prompt_status(id_prompt)

    # Information about the logged user
    user_logged_info = get_jwt_identity()
    logged_user_username = user_logged_info.get('username')
    logged_user_group = get_user_group_id(logged_user_username)

    # Information about the prompt owner user
    prompt_owner_username = get_prompt_owner(id_prompt=id_prompt)
    prompt_owner_user_group = get_user_group_id(prompt_owner_username)

    try:
        if prompt_owner_username == logged_user_username:
            return jsonify(msg="You can't vote your own prompt ")

        if actual_prompt_status not in ['pending', 'review', 'reminder', 'delete']:
            return jsonify(msg=f"This prompt is already {actual_prompt_status}")

        if isInSameGroup(prompt_owner_username, logged_user_username):
            vote_value = 2*VOTING_WEIGHT
            print(prompt_owner_user_group, logged_user_group)
        else:
            print(prompt_owner_user_group, logged_user_group)
            vote_value = 1*VOTING_WEIGHT

        # print(vote_value)
        new_prompt_note = initial_prompt_note + vote_value
        curs.execute("""UPDATE prompts SET note = %s WHERE id = %s""", (new_prompt_note, id_prompt))
        curs.execute("""INSERT INTO votes (prompt_id, user_info, vote_value) VALUES (%s, %s, %s)""", (id_prompt, logged_user_username, vote_value))
        db.commit()

        verif_activation(id=id_prompt, note=new_prompt_note, cursor=curs, database=db)
        return jsonify(msg='Your vote is successfully save')
    except (psycopg2.Error, Exception) as e:
        return jsonify(msg=f"Error : {e}")

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
