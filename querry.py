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
select_all_user_voted_prompt_querry = """SELECT user_info FROM votes where prompt_id=%s"""


# select_info_in_prompt_table_querry = f"""SELECT %s FROM prompts where id=%s"""

# transform_tuple_to_list :
# output a list of tuple --> [('user1',), ('user2',), ('user3',)]
# input a normal list -->    ['user1', 'user2', 'user3']
def transform_tuple_to_list(tuple_data):
    dat_list = []
    for data in tuple_data:
        dat_list.append(data[0])
    return dat_list


# This function get the prompt id and return the username owner
def get_prompt_owner(id_prompt):
    curs.execute("""SELECT user_info FROM prompts where id=%s""", (id_prompt,))
    user = curs.fetchone()  # output --> ('user')
    return user[0]


# This function get actual prompt status
def get_prompt_status(id_prompt):
    curs.execute("""SELECT status FROM prompts where id=%s""", (id_prompt,))
    status = curs.fetchone()  # output --> ('user')
    return status[0]


# This is a function using to get the prompt actual note
def get_prompt_note(id_prompt):
    curs.execute("""SELECT note FROM prompts WHERE id=%s""", (id_prompt,))
    infos = curs.fetchone()  # output --> ('user')
    return infos[0]


#  This is a function using to get the prompt actual price
def get_prompt_price(id_prompt):
    curs.execute("""SELECT price FROM prompts where id=%s""", (id_prompt,))
    infos = curs.fetchone()  # output --> ('user')
    return infos[0]


def get_all_user_voted_prompt(id):
    # Select all user who voted in a same promp
    dict_curs.execute(select_all_user_voted_prompt_querry, (id,))
    user_list = dict_curs.fetchall()
    return user_list


# This function get the group of the user
def get_user_group_id(username):
    curs.execute("""SELECT group_id FROM users where username=%s""", (username,))
    user_group_id = curs.fetchone()  # output --> ('user')
    return user_group_id[0]


# This function return True for same group member and false else
def isInSameGroup(owner, user):
    if get_user_group_id(owner) is None or get_user_group_id(user) is None:
        return False
    else:
        return get_user_group_id(owner) == get_user_group_id(user)


# This function transform selected prompt info to json format
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


# This function  active the prompt in note >=6
def verif_activation(id, note, cursor, database):
    if note >= 6:
        cursor.execute("""UPDATE prompts SET status = 'active' WHERE id = %s""", (id,))
        database.commit()


curs = db.cursor()
dict_curs = db.cursor(cursor_factory=psycopg2.extras.DictCursor)  # This cursor return a list of list --> [[],[]...]

curs.execute(select_all_users_querry)  # Getting all users in user's table
all_users_data = curs.fetchall()  # All users data ( a list of tuple)

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

# select prompts information
dict_curs.execute(select_all_prompt_info_querry)
all_selected_prompts = dict_curs.fetchall()

#  Transform tuple data to list data
all_users_hashed_pass_list = transform_tuple_to_list(all_users_hashed_pass)
all_users_usernames_list = transform_tuple_to_list(all_users_usernames)
all_admins_usernames_list = transform_tuple_to_list(all_admins_usernames)
all_admins_hashed_pass_list = transform_tuple_to_list(all_admins_hashed_pass)

curs.execute('SELECT * FROM admins WHERE username = %s AND hashed_password = %s', ('setoudie', 'try'))
admin = curs.fetchone()

# print(['user1'] in get_all_user_voted_prompt(6))
#
# for elmt in get_all_user_voted_prompt(6):
#     print(elmt)
