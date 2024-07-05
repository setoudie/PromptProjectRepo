from db_conn import get_db_connection

db = get_db_connection(db_name="promptprojectdb")

# Define the querry
select_all_users = """SELECT * FROM users"""


curs = db.cursor()


curs.execute(select_all_users) #Getting all users in user's table
allUsers = curs.fetchall() #all users data ( a list of tuple)
# print(allUsers)


