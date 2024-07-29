# Here we'll define the connection tools for the database

from urllib.parse import urlparse
import psycopg2

LOC_DB_NAME = "promptprojectdb"
HEROKU_DB_NAME = "d3svebcrtcq9m"

# Database connection settings
HEROKU_DATABASE_URL = ("postgres://uaf8jnd2hu15oh:p3a4be1507db6de9ad6a6098edf298909aa8db7bef0e8f4ad8d5595c37dc0cde9"
                       "@cbec45869p4jbu.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d3svebcrtcq9m")

# Extract database connection settings from the URL
"""
    In this file we define a function who create a connection with the database
"""

parsed_url = urlparse(HEROKU_DATABASE_URL)
# print(parsed_url.path)
DB_NAME = parsed_url.path[1:]
USER = parsed_url.username
PASSWORD = parsed_url.password
HOST = parsed_url.hostname
PORT = parsed_url.port


def get_db_connection():
    db = psycopg2.connect(
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    return db
