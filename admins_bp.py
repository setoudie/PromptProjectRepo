from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
def dashboard():
    return "Tableau de bord admin"

@admin_bp.route('/users')
def manage_users():
    return "Gestion des utilisateurs"
