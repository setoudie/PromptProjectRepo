import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import psycopg2.extras
from db_conn import get_db_connection

create_table = """
-- Create admins table if it does not exist
CREATE TABLE IF NOT EXISTS public.admins
(
    username        VARCHAR(20) NOT NULL
        PRIMARY KEY,
    firstname       VARCHAR(25),
    lastname        VARCHAR(25),
    hashed_password VARCHAR(300)
);

ALTER TABLE public.admins
    OWNER TO my_prompt_project_admin;

-- Create groups table if it does not exist
CREATE TABLE IF NOT EXISTS public.groups
(
    id         SERIAL PRIMARY KEY,
    group_name VARCHAR(25) NOT NULL UNIQUE,
    admin_info VARCHAR(20)
        REFERENCES public.admins (username)
);

ALTER TABLE public.groups
    OWNER TO my_prompt_project_admin;

-- Create users table if it does not exist
CREATE TABLE IF NOT EXISTS public.users
(
    username        VARCHAR(20) NOT NULL
        PRIMARY KEY,
    firstname       VARCHAR(25),
    lastname        VARCHAR(25),
    hashed_password VARCHAR(300),
    group_id        INTEGER
        REFERENCES public.groups (id),
    admin_info      VARCHAR(20)
        REFERENCES public.admins (username)
);

ALTER TABLE public.users
    OWNER TO my_prompt_project_admin;

-- Create prompts table if it does not exist
CREATE TABLE IF NOT EXISTS public.prompts
(
    id             SERIAL PRIMARY KEY,
    prompt_content TEXT,
    price          DOUBLE PRECISION DEFAULT 1000,
    note           INTEGER DEFAULT 0
        CONSTRAINT prompts_note_check
            CHECK (note >= -10 AND note <= 10),
    status         VARCHAR(10) DEFAULT 'pending'
        CONSTRAINT prompts_status_check
            CHECK (status IN ('active', 'inactive', 'pending', 'review', 'reminder', 'delete')),
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_info      VARCHAR(20)
        REFERENCES public.users (username)
);

ALTER TABLE public.prompts
    OWNER TO my_prompt_project_admin;

-- Create notes table if it does not exist
CREATE TABLE IF NOT EXISTS public.notes
(
    id         SERIAL PRIMARY KEY,
    prompt_id  INTEGER
        REFERENCES public.prompts (id)
        ON DELETE CASCADE,
    user_info  VARCHAR(20)
        REFERENCES public.users (username),
    note_value DOUBLE PRECISION
);

ALTER TABLE public.notes
    OWNER TO my_prompt_project_admin;

-- Create votes table if it does not exist
CREATE TABLE IF NOT EXISTS public.votes
(
    id         SERIAL PRIMARY KEY,
    prompt_id  INTEGER
        REFERENCES public.prompts (id)
        ON DELETE CASCADE,
    user_info  VARCHAR(20)
        REFERENCES public.users (username),
    vote_value INTEGER
);

ALTER TABLE public.votes
    OWNER TO my_prompt_project_admin;

-- Create function to update prompts state if it does not exist
CREATE OR REPLACE FUNCTION public.update_prompts_state() RETURNS TRIGGER
    LANGUAGE plpgsql
AS
$$
BEGIN
    UPDATE prompts
    SET status = 'review'
    WHERE status = 'pending'
    AND created_at < NOW() - INTERVAL '1 hours';
    RETURN NEW;
END;
$$;

ALTER FUNCTION public.update_prompts_state() OWNER TO my_prompt_project_admin;

-- Create trigger to update prompts state if it does not exist
CREATE TRIGGER IF NOT EXISTS trg_update_prompts_state
    AFTER INSERT OR UPDATE
    ON public.prompts
    FOR EACH ROW
EXECUTE FUNCTION public.update_prompts_state();

"""
LOC_DB_NAME = "promptprojectdb"
HEROKU_DB_NAME = "d3svebcrtcq9m"

db = get_db_connection()

# Define the querry
select_all_users_querry = """SELECT * FROM users"""
select_prompt_sell_info_querry = """SELECT prompt_content, user_info, price FROM prompts WHERE id=%s"""
select_all_users_usernames_querry = """SELECT username FROM users"""
select_all_users_hashed_password_querry = """SELECT hashed_password FROM users"""
select_all_user_noted_prompt_querry = """SELECT user_info FROM notes WHERE prompt_id=%s"""

select_all_admin_usernames_querry = """SELECT username FROM admins"""
select_all_hashed_admins_password_querry = """SELECT hashed_password FROM admins"""

select_all_prompt_info_querry = """SELECT prompt_content, user_info, price, note, status FROM prompts"""
select_user_vote_value_querry = """SELECT vote_value FROM votes WHERE prompt_id=%s"""
select_all_user_voted_prompt_querry = """SELECT user_info FROM votes WHERE prompt_id=%s"""
update_prompt_status_every_day = """
                                        UPDATE prompts
                                        SET status = 'review'
                                        WHERE status IN ('pending', 'delete')
                                        AND creat_at < NOW() - INTERVAL '2 days'
                                 """


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
    # Select all user who voted in a same prompt
    dict_curs.execute(select_all_user_voted_prompt_querry, (id,))
    user_list = dict_curs.fetchall()
    return user_list


# This function get all user noted to the specific prompt with id: id
def get_all_user_noted_prompt(id):
    # Select all user who voted in a same prompt
    dict_curs.execute(select_all_user_noted_prompt_querry, (id,))
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


# This function update the vote value of prompt and add vote info into table vote
def update_prompt_vote_value(cursor, database, id_prompt, logged_user_username, prompt_owner_username,
                             initial_prompt_note, weight):
    # cursor = db.cursor()
    if isInSameGroup(prompt_owner_username, logged_user_username):
        vote_value = 2 * weight
        print("Users are in the same group:", prompt_owner_username, logged_user_username)
    else:
        vote_value = 1 * weight
        print("Users are in different groups:", prompt_owner_username, logged_user_username)

    new_prompt_note = initial_prompt_note + vote_value

    # Mettre à jour la note du prompt
    cursor.execute("""UPDATE prompts SET note = %s WHERE id = %s""", (new_prompt_note, id_prompt))

    # Insérer le vote dans la table des votes
    cursor.execute("""INSERT INTO votes (prompt_id, user_info, vote_value) VALUES (%s, %s, %s)""",
                   (id_prompt, logged_user_username, vote_value))

    database.commit()  # Save the changes
    verif_deletion(id=id_prompt, note=new_prompt_note, cursor=curs, database=database)
    verif_activation(id=id_prompt, note=new_prompt_note, cursor=curs, database=database)


def update_prompt_price(cursor, database, id_prompt, logged_user_username, prompt_owner_username,
                        initial_prompt_price, input_user_note):
    default_price = 1000
    # cursor = db.cursor()
    if isInSameGroup(prompt_owner_username, logged_user_username):
        note_value = 0.6 * input_user_note
        print("Users are in the same group:", prompt_owner_username, logged_user_username)
    else:
        note_value = 0.4 * input_user_note
        print("Users are in different groups:", prompt_owner_username, logged_user_username)

    # new_prompt_price = initial_prompt_price + vote_value

    # Insérer le vote dans la table des votes
    cursor.execute("""INSERT INTO notes (prompt_id, user_info, note_value) VALUES (%s, %s, %s)""",
                   (id_prompt, logged_user_username, note_value))
    database.commit()  # Save the changes

    # calculate the sum of notes
    cursor.execute("""SELECT SUM(note_value) FROM notes WHERE prompt_id = %s""", (id_prompt,))
    avg_notes = cursor.fetchone()[0]
    print(avg_notes)

    # Count all user who rate a specific prompt
    cursor.execute("""SELECT COUNT(user_info) FROM notes WHERE prompt_id = %s""", (id_prompt,))
    total_user_noted_prompt = cursor.fetchone()[0]
    print(total_user_noted_prompt, initial_prompt_price)

    new_price = round(default_price * (1 + (avg_notes / total_user_noted_prompt)), 2)
    print(new_price)

    # Update the price  of the prompt
    cursor.execute("""UPDATE prompts SET price = %s WHERE id = %s""", (new_price, id_prompt))
    database.commit()


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
        } for item in data
    ]
    return json_data


# This function  active the prompt when note >=6
def verif_activation(id, note, cursor, database):
    if note >= 6:
        cursor.execute("""UPDATE prompts SET status = 'active' WHERE id = %s""", (id,))
        database.commit()


# This function change prompt status to delete when note <=-6
def verif_deletion(id, note, cursor, database):
    if note <= -6:
        cursor.execute("""UPDATE prompts SET status = 'delete' WHERE id = %s""", (id,))
        database.commit()


# This function get the vote value of user with id = id
def get_user_vote_value(id, cursor, database):
    cursor.execute(select_user_vote_value_querry, (id,))
    data = cursor.fetchone()
    database.commit()
    return data[0]


def send_prompt(sender, passw, receiver, subject, msg):
    try:
        # Création du message MIME
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject

        # Attacher le corps du message
        message.attach(MIMEText(msg, 'plain'))

        # Connexion au serveur SMTP et envoi du mail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, passw)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()

        print(f"Message successfully sent to {receiver}")
    except Exception as e:
        print(f"Failed to send message: {e}")
        raise


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

curs.execute(select_prompt_sell_info_querry, (13,))
admin = curs.fetchall()

# print(transform_data_to_json(admin))

# update_prompt_vote_value(curs, db, 11, "user1", "user11", 1, 1)
