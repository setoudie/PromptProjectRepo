from flask import Blueprint

users_bp = Blueprint('users', __name__)


@users_bp.route('/list')
def user_list():
    return 'users list'
