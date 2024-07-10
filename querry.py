import json
import psycopg2.extras
from db_conn import get_db_connection

db = get_db_connection(db_name="promptprojectdb")

# Define the querry
select_all_users_querry = """SELECT * FROM users"""
select_all_users_usernames_querry = """SELECT username FROM users"""
select_all_admin_usernames_querry = """SELECT username FROM admins"""
select_all_users_hashed_password_querry = """SELECT hashed_password FROM users"""
select_all_hashed_admins_password_querry = """SELECT hashed_password FROM admins"""
select_all_prompt_info_querry = """SELECT prompt_content, user_info, price, note, status FROM prompts"""


# transform_tuple_to_list :
# output a list of tuple --> [('user1',), ('user2',), ('user3',)]
# input a normal list -->    ['user1', 'user2', 'user3']
def transform_tuple_to_list(tuple_data):
    dat_list = []
    for data in tuple_data:
        dat_list.append(data[0])
    return dat_list


# This fonction transform selected prompt info to json format
def transform_data_to_json(data):
    """
    Transforme une liste de tuples en une liste de dictionnaires formatée en JSON.

    :param data: Liste de tuples
    :return: JSON formaté
    """
    json_data = [
        {
            'content': item[0],
            'owner': item[1],
            'price': item[2],
            'status': item[4]
        } for item in data
    ]

    return json.dumps(json_data)


curs = db.cursor()
dict_curs = db.cursor(cursor_factory=psycopg2.extras.DictCursor)

curs.execute(select_all_users_querry)  #Getting all users in user's table
all_users_data = curs.fetchall()  #all users data ( a list of tuple)

# Selecting all user's username
curs.execute(select_all_users_usernames_querry)
all_users_usernames = curs.fetchall()
# print(all_users_usernames)   #--> [('user1',), ('user2',), ('user3',)]

# Selecting all user's hashed password
curs.execute(select_all_users_hashed_password_querry)
all_users_hashed_pass = curs.fetchall()

# Select all admins usernames
curs.execute(select_all_admin_usernames_querry)
all_admins_usernames = curs.fetchall()

# Selecting all admins hashed password
curs.execute(select_all_hashed_admins_password_querry)
all_admins_hashed_pass = curs.fetchall()

# select prompts informations
dict_curs.execute(select_all_prompt_info_querry)
all_selected_prompts = dict_curs.fetchall()


#  Transform tuple data to list data
all_users_hashed_pass_list = transform_tuple_to_list(all_users_hashed_pass)
all_users_usernames_list = transform_tuple_to_list(all_users_usernames)
all_admins_usernames_list = transform_tuple_to_list(all_admins_usernames)
all_admins_hashed_pass_list = transform_tuple_to_list(all_admins_hashed_pass)

curs.execute('SELECT * FROM admins WHERE username = %s AND hashed_password = %s', ('setoudie', 'try'))
admin = curs.fetchone()

print(all_selected_prompts)
