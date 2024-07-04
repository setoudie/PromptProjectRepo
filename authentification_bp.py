from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return "Page de connexion"

@auth_bp.route('/logout')
def logout():
    return "Page de déconnexion"
