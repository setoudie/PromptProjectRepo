from flask import Blueprint

groups_bp = Blueprint('groups', __name__)

@groups_bp.route('/create')
def create_group():
    return "Page de création de groupe"

@groups_bp.route('/list')
def list_groups():
    return "Liste des groupes"
