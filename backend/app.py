from flask import render_template, request
from blueprint import create_app
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from querry import update_prompt_status_every_day, create_table
from db_conn import get_db_connection

LOC_DB_NAME = "promptprojectdb"
HEROKU_DB_NAME = "d3svebcrtcq9m"


# Fonction pour mettre à jour le statut des prompts dans la base de données
def automatically_run_function():
    # db = get_db_connection()
    # curs = db.cursor()
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
    return "<h1>render_template('backend/templates/login.html')</h1>"


if __name__ == '__main__':
    try:
        db = get_db_connection()
        curs = db.cursor()
        curs.execute(create_table)
        db.commit()
        app.run(debug=True)
    finally:
        scheduler.shutdown()
