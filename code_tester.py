from werkzeug.security import generate_password_hash, check_password_hash
from querry import all_users_data

#print(dict(zip(['id', 'username', 'firstname', 'lastname', 'password', 'group_id'], (93, 'user3', 'dolo', 'yaap', 'passer', 1))))

print(all_users_data)

hash_pass = generate_password_hash('passer')
print(hash_pass)
print(check_password_hash(pwhash=hash_pass, password='passer'))

# user = 'user1'
for user in all_users_data:
    print(user)
else:
    print("Not Good")