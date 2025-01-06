-- Requette SQL pour creer ma base de donne
CREATE TABLE IF NOT EXISTS public.admins
(
    username        VARCHAR(20) NOT NULL
        PRIMARY KEY,
    firstname       VARCHAR(25),
    lastname        VARCHAR(25),
    hashed_password VARCHAR(300)
);


-- Create groups table if it does not exist
CREATE TABLE IF NOT EXISTS public.groups
(
    id         SERIAL PRIMARY KEY,
    group_name VARCHAR(25) NOT NULL UNIQUE,
    admin_info VARCHAR(20)
        REFERENCES public.admins (username)
);


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
