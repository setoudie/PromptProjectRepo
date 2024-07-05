from db_conn import get_db_connection

db = get_db_connection(db_name="promptprojectdb")

# Define the querry
select_all_users = """SELECT * FROM users"""
select_all_users_usernames = """SELECT username FROM users"""
select_all_admin_usernames = """SELECT username FROM admins"""
select_all_users_hashed_password = """SELECT hashed_password FROM users"""
select_all_hashed_admins_password = """SELECT hashed_password FROM admins"""


# transform_tuple_to_list :
# output a list of tuple --> [('user1',), ('user2',), ('user3',)]
# input a normal list -->    ['user1', 'user2', 'user3']
def transform_tuple_to_list(tuple_data):
    dat_list = []
    for data in tuple_data:
        dat_list.append(data[0])
    return dat_list

curs = db.cursor()

curs.execute(select_all_users)  #Getting all users in user's table
all_users_data = curs.fetchall()  #all users data ( a list of tuple)

# Selecting all user's username
curs.execute(select_all_users_usernames)
all_users_usernames = curs.fetchall()
# print(all_users_usernames)   #--> [('user1',), ('user2',), ('user3',)]

# Selecting all user's hashed password
curs.execute(select_all_users_hashed_password)
all_users_hashed_pass = curs.fetchall()

# Select all admin's usernames
curs.execute(select_all_admin_usernames)
all_admins_usernames = curs.fetchall()

# Selecting all admin's hashed password
curs.execute(select_all_hashed_admins_password)
all_admins_hashed_pass = curs.fetchall()

all_users_hashed_pass_list = transform_tuple_to_list(all_users_hashed_pass)
all_users_usernames_list = transform_tuple_to_list(all_users_usernames)
all_admins_usernames_list = transform_tuple_to_list(all_admins_usernames)
all_admins_hashed_pass_list = transform_tuple_to_list(all_admins_hashed_pass)

print(all_admins_hashed_pass_list)