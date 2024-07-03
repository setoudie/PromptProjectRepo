# Here we'll define the connection tools for the database

import psycopg2


def get_db_connection(db_name):
    # Database information
    # DATABASE = "test"
    USER = "my_prompt_project_admin"
    HOST = 'localhost'
    PASS = "wrongpassword"

    # Connection to database
    db = psycopg2.connect(database=db_name,
                          user=USER,
                          host=HOST,
                          password=PASS)
    return db
