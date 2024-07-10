from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from authentification_bp import role_required
from querry import transform_data_to_json, all_selected_prompts
prompts_bp = Blueprint('prompts', __name__)


@prompts_bp.route('/create')
def create_prompt():
    return "Page de création de prompt"


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
