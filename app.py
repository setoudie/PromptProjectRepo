from flask import render_template, request
from blueprint import create_app
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from querry import update_prompt_status_every_day
from db_conn import get_db_connection


# Fonction pour mettre à jour le statut des prompts dans la base de données
def automatically_run_function():
    db = get_db_connection("promptprojectdb")
    curs = db.cursor()
    curs.execute(update_prompt_status_every_day)
    curs.close()
    db.commit()
    print(f"Message imprimé à : {datetime.now()}")


# Configuration et démarrage du planificateur pour exécuter la fonction toutes les 1 jours
scheduler = BackgroundScheduler()
scheduler.add_job(automatically_run_function, 'interval', hours=1)
scheduler.start()

app = create_app()


@app.route('/')
def home():
    return "<h1>render_template('login.html')</h1>"


if __name__ == '__main__':
    try:
        app.run(debug=True)
    finally:
        scheduler.shutdown()
