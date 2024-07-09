from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from authentification_bp import role_required
groups_bp = Blueprint('groups', __name__)

@groups_bp.route('/create', methods=['POST'])
@jwt_required()
@role_required('ad min')
def creat_group():
    return jsonify(msg='Group Creer')

@groups_bp.route('/list')
def list_groups():
    return "Liste des groupes"
