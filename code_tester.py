from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


# Fonction de test
def print_message():
    print(f"Message imprimé à : {datetime.now()}")


# Configuration du planificateur
scheduler = BlockingScheduler()
scheduler.add_job(print_message, 'interval', seconds=10)

# Démarrage du planificateur
print("Scheduler démarré. Le message sera imprimé toutes les minutes.")
scheduler.start()
