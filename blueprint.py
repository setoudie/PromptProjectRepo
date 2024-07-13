from flasgger import Swagger
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from authentification_bp import auth_bp
from users_bp import users_bp
from admins_bp import admin_bp
from groups_bp import groups_bp
from prompts_bp import prompts_bp

# Fonction de creation de l'app and all bluprints
def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.config['JWT_SECRET_KEY'] = 'fd06cd22f58b414a91c68a59ea4f351e'
    jwt = JWTManager(app)

    # Enregistrer les blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(admin_bp, url_prefix='/admins')
    app.register_blueprint(groups_bp, url_prefix='/groups')
    app.register_blueprint(prompts_bp, url_prefix='/prompts')

    return app

