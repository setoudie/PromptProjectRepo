import yagmail


def send_email(from_email, to_email, subject, body, password):
    try:
        # Initialisation de yagmail avec l'adresse email et le mot de passe
        yag = yagmail.SMTP(from_email, password)

        # Envoi de l'email
        yag.send(
            to=to_email,
            subject=subject,
            contents=body
        )
        print("Email envoyé avec succès")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")


# Exemples d'utilisation
from_email = "votre_email@gmail.com"
to_email = "destinataire@example.com"
subject = "Sujet de l'email"
body = "Ceci est le corps de l'email."
password = "votre_mot_de_passe"

send_email(from_email, to_email, subject, body, password)
