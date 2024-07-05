from db_conn import get_db_connection

db = get_db_connection(db_name="promptprojectdb")

# Define the querry
select_all_users = """SELECT * FROM users"""
select_all_usernames = """SELECT username FROM users"""


curs = db.cursor()


curs.execute(select_all_users) #Getting all users in user's table
allUsers = curs.fetchall() #all users data ( a list of tuple)

curs.execute(select_all_usernames)
allUserNames = curs.fetchall()
# print(allUserNames)   #--> [('user1',), ('user2',), ('user3',)]

allUserNames_list = []
for username in allUserNames:
    allUserNames_list.append(username[0])
#print(allUserNames_list) #--> ['user1', 'user2', 'user3']
