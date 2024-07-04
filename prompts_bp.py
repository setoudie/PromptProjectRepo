from flask import Blueprint

prompts_bp = Blueprint('prompts', __name__)


@prompts_bp.route('/create')
def create_prompt():
    return "Page de création de prompt"


@prompts_bp.route('/list')
def list_prompts():
    return "Liste des prompts"
