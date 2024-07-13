from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/api/example', methods=['GET'])
def example():
    """
    Exemple d'endpoint
    ---
    responses:
      200:
        description: Un message de succès
    """
    return {"message": "Succès"}

if __name__ == "__main__":
    app.run()
