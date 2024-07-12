from functools import wraps
from flask_jwt_extended import decode_token, jwt_required
from flask import Flask, request, jsonify, make_response, session, render_template, Blueprint
from datetime import timedelta

from jwt import ExpiredSignatureError, InvalidTokenError

from blueprint import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/protected-route', methods=['GET'])
@jwt_required()
def protected_route():
    # Code de la route protégée
    return jsonify({'message': 'good'})


if __name__ == '__main__':
    app.run(debug=True)
