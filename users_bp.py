from flask import Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from querry import allUsers

users_bp = Blueprint('users', __name__)


