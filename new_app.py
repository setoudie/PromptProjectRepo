import smtplib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Fonction pour envoyer un email
def send_prompt(sender, passw, receiver, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, passw)
        server.sendmail(sender, receiver, msg)
        server.quit()
        print(f"Message successfully sent to {receiver}")
    except Exception as e:
        print(f"Failed to send message: {e}")
        raise

@app.route('/buy/<int:id_prompt>', methods=["GET"])
def buy_prompt(id_prompt):
    try:
        from_addr = "senytoutou@gmail.com"
        key_pass = "rxghihsffciuriby"
        to_addr = request.json.get('email')

        if not to_addr:
            return jsonify(msg="Email address is required"), 400

        # Simulez la requête à la base de données
        # Remplacez par votre propre logique de récupération de données
        select_prompt_sell_info_query = "YOUR QUERY HERE"
        curs.execute(select_prompt_sell_info_query, (id_prompt,))
        message = transform_data_to_json(curs.fetchall())

        send_prompt(sender=from_addr, passw=key_pass, receiver=to_addr, msg=message)
        return jsonify(msg='Check your mail, the prompt is sent')

    except Exception as e:
        return jsonify(msg=f"An error occurred: {e}"), 500

def transform_data_to_json(data):
    # Transforme les données en JSON (à adapter selon votre cas)
    return str(data)

# Simulez la configuration de la base de données et le curseur
class MockCursor:
    def execute(self, query, params):
        pass

    def fetchall(self):
        return [{"id": 1, "name": "Prompt 1"}]

curs = MockCursor()

if __name__ == "__main__":
    app.run(debug=True)
