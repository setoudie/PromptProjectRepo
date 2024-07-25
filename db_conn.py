# Here we'll define the connection tools for the database
LOC_DB_NAME = "promptprojectdb"
HEROKU_DB_NAME = "d3svebcrtcq9m"
import psycopg2

# Database connection settings
DATABASE_URL = "postgres://uaf8jnd2hu15oh:p3a4be1507db6de9ad6a6098edf298909aa8db7bef0e8f4ad8d5595c37dc0cde9@cbec45869p4jbu.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d3svebcrtcq9m"

# Extract database connection settings from the URL
from urllib.parse import urlparse

parsed_url = urlparse(DATABASE_URL)
DB_NAME = parsed_url.path[1:]
USER = parsed_url.username
HOST = parsed_url.hostname
PORT = parsed_url.port
PASS = parsed_url.password
print(PASS)


# DATABASE = "test"
# USER = "my_prompt_project_admin"
# HOST = 'localhost'
# PASS = "wrongpassword"
# Here we'll define the connection tools for the database

# Define a function to get a database connection
def get_db_connection(db_name=DB_NAME):
    # Connection to database
    db = psycopg2.connect(
        database=db_name,
        user=USER,
        host=HOST,
        password=PASS,
        port=PORT
    )
    return db
