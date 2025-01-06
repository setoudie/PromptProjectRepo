from db_conn import *
from querry import select_all_users_querry

conn = get_db_connection()
curs = conn.cursor()
curs.execute(select_all_users_querry)
print(curs.fetchall())
# print(conn)