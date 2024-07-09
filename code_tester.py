from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import decode_token
from querry import all_users_data, all_users_usernames_list, all_users_hashed_pass_list
#print(dict(zip(['id', 'username', 'firstname', 'lastname', 'password', 'group_id'], (93, 'user3', 'dolo', 'yaap', 'passer', 1))))

# print(all_users_data)
#
# hash_pass = generate_password_hash('passer')
# print(hash_pass)
# print(check_password_hash(pwhash=hash_pass, password='passer'))

# print(all_users_usernames_list)
# user = 'user1'
# for index, username in enumerate(all_users_usernames_list):
#     print(username.index(username))

user_info = (1, 'user1', 'fatou', 'dieng', 'scrypt:32768:8:1$dIfmtgoE1tEXyUii$f446f78de014046d8f3fb022c83632b2fe266a2ff6e98121bb0bc0f705910c90566d036b434b7261f4ac6e1007c80643b8a754cd82ca0573289e9e0851896ca8', None)  # Exemple de liste d'utilisateurs
test_pass = 'passer'

# test de la fonction pour verifier l'auth de l'user
for username, hash_pass in zip(all_users_usernames_list, all_users_hashed_pass_list):
    if username == user_info[1]:
        index = all_users_usernames_list.index(username)
        print(index, end=' ')
        print(check_password_hash(pwhash=user_info[-2], password=test_pass))
        print(user_info[-2])

### TEST CODE POUR LES AUTORISATION

from flask_jwt_extended import decode_token
from jwt.exceptions import InvalidTokenError

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMDQ1MTc1NSwianRpIjoiMmQzODI5N2UtZjM5MC00ZDZkLTgyNGQtYjExNWJlMDFiZTcyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VybmFtZSI6InVzZXIxIiwicm9sZSI6InVzZXIifSwibmJmIjoxNzIwNDUxNzU1LCJjc3JmIjoiNjZhMzQwNGItNWE5YS00MDRmLTg0NWItM2U2ZmI1YWY0ODk2IiwiZXhwIjoxNzIwNDUyNjU1fQ.USi_bic0fdcPd6Q4uyH8Mj_JGf_j2OFPo_GexDprjY"

try:
    decoded_token = decode_token(token)
    print(decoded_token)
except InvalidTokenError as e:
    print(f"Erreur lors de la vérification du token : {e}")
