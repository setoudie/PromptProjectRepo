from db_conn import get_db_connection

db = get_db_connection(db_name="test")

curs = db.cursor()
curs.execute("""SELECT * FROM table_test""")
rows = curs.fetchall()
print(rows)
