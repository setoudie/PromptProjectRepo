from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, verify_jwt_in_request
from functools import wraps

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'toto'  # Changez cela avec une clé secrète plus sécurisée
jwt = JWTManager(app)


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_identity()
            if claims.get('role') != role:
                return jsonify({'msg': 'Forbidden: Insufficient permissions'}), 403
            return fn(*args, **kwargs)

        return decorator

    return wrapper


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Ajoutez ici la logique de vérification de l'utilisateur
    if username != 'admin' or password != 'admin':  # Exemple de vérification simple
        return jsonify({"msg": "Bad username or password"}), 401

    # Créer un token JWT avec le rôle 'admin'
    access_token = create_access_token(identity={'username': username, 'role': 'admin'})
    return jsonify(access_token=access_token)


@app.route('/create_group', methods=['POST'])
@jwt_required()
@role_required('admin')
def create_group():
    # Code pour créer un groupe
    return jsonify(msg='Group created successfully'), 201


if __name__ == '__main__':
    app.run()
