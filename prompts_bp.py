from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from authentification_bp import role_required
from db_conn import get_db_connection
from querry import transform_data_to_json, all_selected_prompts
prompts_bp = Blueprint('prompts', __name__)


@prompts_bp.route('/create', methods=['POST'])
@jwt_required()
@role_required('user')
def create_prompt():
    content = request.json.get('content')
    user_info = get_jwt_identity()
    username_user = user_info.get('username')
    print(username_user)
    if content:
        db = get_db_connection('promptprojectdb')
        curs = db.cursor()
        curs.execute("""INSERT INTO prompts (prompt_content, user_info) VALUES (%s, %s)""", (content, username_user))
        db.commit()
        db.close()
        return jsonify(msg='Prompt succesfuly create')
    else:
        return jsonify(msg='Missing values')
    # return "Page de création de prompt"


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
