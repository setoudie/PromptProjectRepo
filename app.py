from flask import Flask, request, jsonify, make_response, session, render_template, Blueprint
from datetime import timedelta
from blueprint import create_app

app = create_app()

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)

