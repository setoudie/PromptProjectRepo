import psycopg2
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from authentification_bp import role_required
from db_conn import get_db_connection
from querry import transform_data_to_json, all_selected_prompts, get_prompt_owner, get_user_group_id, get_prompt_price, \
    get_prompt_note, get_prompt_status, isInSameGroup, verif_activation, get_all_user_voted_prompt, get_user_vote_value, \
    verif_deletion, update_prompt_vote_value, get_all_user_noted_prompt, update_prompt_price

prompts_bp = Blueprint('prompts', __name__)

db = get_db_connection('promptprojectdb')
curs = db.cursor()


# Route pour creer un prompt et le proposer a vendre
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
        return jsonify(msg='Prompt successfully create')
    else:
        return jsonify(msg='Missing values')


# This route can is used to edit a prompt
@prompts_bp.route('/edit/<int:id_prompt>', methods=['PUT'])
@jwt_required()
@role_required('user')
def edit_prompt(id_prompt):
    user_info = get_jwt_identity()
    logged_username = user_info.get('username')

    try:
        if get_prompt_owner(id_prompt=id_prompt) == logged_username:
            if get_prompt_status(id_prompt=id_prompt) in ['pending', 'review']:
                new_prompt_content = request.json.get('new_content')
                curs.execute("""UPDATE prompts SET prompt_content = %s WHERE id = %s""",
                             (new_prompt_content, id_prompt))
                db.commit()
                return jsonify(msg="Your update is successfully save")
            else:
                return jsonify(msg=f"You can't update a prompt with {get_prompt_status(id_prompt)} status")
        else:
            return jsonify(msg="You can also vote your own prompt")
    except TypeError:
        return jsonify(msg="Missing id")
    except psycopg2.Error as e:
        return jsonify(msg=f"Error : {e}")


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


# Route pour demander a l'user de modifier son prompt
@prompts_bp.route('/ask-to-edit/<int:id_prompt>', methods=['PUT'])
@jwt_required()
@role_required('admin')
def prompt_asked_to_edited(id_prompt):
    admin_info = get_jwt_identity()
    username = admin_info.get('username')

    try:
        if username:
            curs.execute("""UPDATE prompts SET status = 'review' WHERE id = %s""", (id_prompt,))
            db.commit()
            # db.close()
            return jsonify(msg='Prompt Successfully added to to review prompt')
    except Exception as e:
        return jsonify(msg=f'Error : {e}')


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


# Route pour liker un prompt
@prompts_bp.route('/like/<int:id_prompt>', methods=['PUT', 'GET'])
@jwt_required()
@role_required('user')
def like_vote(id_prompt):
    LIKE_VOTING_WEIGHT = 1
    # curs = db.cursor()
    try:
        initial_prompt_note = get_prompt_note(id_prompt)
    except TypeError:
        return jsonify(msg=f"Not prompt with id = {id_prompt}")

    actual_prompt_status = get_prompt_status(id_prompt)

    # Information about the logged user
    user_logged_info = get_jwt_identity()
    logged_user_username = user_logged_info.get('username')

    # Information about the prompt owner user
    prompt_owner_username = get_prompt_owner(id_prompt=id_prompt)

    # Check if the user is already vote the prompt
    if [logged_user_username] in get_all_user_voted_prompt(id=id_prompt) and 0 <= get_user_vote_value(id=id_prompt,
                                                                                                      cursor=curs,
                                                                                                      database=db):
        return jsonify(msg="You can't vote again. You're already vote this prompt")
    else:
        try:
            if prompt_owner_username == logged_user_username:
                return jsonify(msg="You can't vote your own prompt ")

            if actual_prompt_status not in ['pending', 'delete']:
                return jsonify(msg=f"Prompt status: {actual_prompt_status}\n You can't vote this prompt")

            # This function is explained in 'querry.py' file
            update_prompt_vote_value(curs, db, id_prompt, logged_user_username, prompt_owner_username,
                                     initial_prompt_note, LIKE_VOTING_WEIGHT)

            return jsonify(msg='Your vote is successfully save')
        except (psycopg2.Error, Exception) as e:
            return jsonify(msg=f"Error : {e}")


# Route pour dislike un prompt
@prompts_bp.route('/dislike/<int:id_prompt>', methods=['PUT', 'GET'])
@jwt_required()
@role_required('user')
def dislike_vote(id_prompt):
    DISLIKE_VOTING_WEIGHT = -1
    # curs = db.cursor()
    try:
        initial_prompt_note = get_prompt_note(id_prompt)

    except TypeError:  # if the id is missing get_prompt_note return None so i catch this error
        return jsonify(msg=f"Not prompt with id = {id_prompt}")

    actual_prompt_status = get_prompt_status(id_prompt)

    # Information about the logged user : (username and group)
    user_logged_info = get_jwt_identity()
    logged_user_username = user_logged_info.get('username')

    # Information about the prompt owner user: (username and group)
    prompt_owner_username = get_prompt_owner(id_prompt=id_prompt)

    # Check if the user is already vote the prompt
    if [logged_user_username] in get_all_user_voted_prompt(id=id_prompt) and get_user_vote_value(id=id_prompt,
                                                                                                 cursor=curs,
                                                                                                 database=db) < 0:
        return jsonify(msg="You can't vote again. You're already vote this prompt")
    else:
        try:
            if prompt_owner_username == logged_user_username:
                return jsonify(msg="You can't vote your own prompt ")

            if actual_prompt_status not in ['active', 'pending']:
                return jsonify(msg=f"Prompt status: {actual_prompt_status}\n You can't vote this prompt")
                # This function is explained in 'querry.py' file
            else:
                update_prompt_vote_value(curs, db, id_prompt, logged_user_username, prompt_owner_username,
                                         initial_prompt_note, DISLIKE_VOTING_WEIGHT)

                return jsonify(msg='Your vote is successfully save')
        except (psycopg2.Error, Exception) as e:
            return jsonify(msgs=f"Error : {e}")


# Route pour noter un prompt afin de changer le prix
@prompts_bp.route('/rate/<int:id_prompt>', methods=['PUT', 'GET'])
@jwt_required()
@role_required('user')
def rate_prompt(id_prompt):
    # LIKE_VOTING_WEIGHT = 1
    # curs = db.cursor()
    try:
        initial_prompt_price = get_prompt_price(id_prompt)
    except TypeError:
        return jsonify(msg=f"Not prompt with id = {id_prompt}")

    actual_prompt_status = get_prompt_status(id_prompt)

    # Information about the logged user
    user_logged_info = get_jwt_identity()
    logged_user_username = user_logged_info.get('username')

    # Information about the prompt owner user
    prompt_owner_username = get_prompt_owner(id_prompt=id_prompt)

    # Check if the user is already vote the prompt
    if [logged_user_username] in get_all_user_noted_prompt(id=id_prompt):
        return jsonify(msg="You're already rate this prompt")
    else:
        try:
            if prompt_owner_username == logged_user_username:
                return jsonify(msg="You can't rate your own prompt ")

            if actual_prompt_status not in ['active']:
                return jsonify(msg=f"Prompt status: {actual_prompt_status}\n You can't rate this prompt")

            note = request.json.get('note')

            if not (-10 <= note <= 10):
                return jsonify(msg='Only values between -10 and 10 are authorized')
            else:
                # This function is explained in 'querry.py' file
                update_prompt_price(curs, db, id_prompt, logged_user_username, prompt_owner_username,
                                    initial_prompt_price, note)

            return jsonify(msg='Your vote is successfully save')
        except (psycopg2.Error, Exception) as e:
            return jsonify(msg=f"Error : {e}")


# Route pour afficher tous les prompts
@prompts_bp.route('/dashboard', methods=['GET'])
@jwt_required()
# @role_required('admin')
# @role_required('user')
def show_all_prompts():
    json_data = [
        {
            'content': item[0],
            'owner': item[1],
            'price': item[2],
            'status': item[4]
        } for item in all_selected_prompts]
    return jsonify(json_data)
