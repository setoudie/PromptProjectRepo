-- Creation de la table Admin
CREATE TABLE IF NOT EXISTS Admins(
    username VARCHAR(20) UNIQUE NOT NULL PRIMARY KEY,
    firstname VARCHAR(25),
    lastname  VARCHAR(25),
    password VARCHAR(100)
);

-- Creation de la table UserGroup
CREATE TABLE IF NOT EXISTS Groups(
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(25) UNIQUE NOT NULL
);

-- Creation de la table User
CREATE TABLE IF NOT EXISTS Users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    firstname VARCHAR(25),
    lastname  VARCHAR(25),
    password VARCHAR(100),
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES Groups(id)

);

-- Creation de la table Prompt
CREATE TABLE IF NOT EXISTS Prompts(
    id SERIAL PRIMARY KEY,
    category VARCHAR(30),
    prompt_content TEXT,
    price FLOAT,
    note INTEGER,
    status VARCHAR(10) CHECK (status IN ('active', 'inactive', 'pending', 'review', 'reminder', 'delete')) DEFAULT 'pending',
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Creation de la table Notes
CREATE TABLE IF NOT EXISTS Notes(
    id SERIAL PRIMARY KEY,
    prompt_id  INTEGER,
    user_id INTEGER,
    note_value FLOAT,
    FOREIGN KEY (prompt_id) REFERENCES Prompts(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Creation de la table Votes
CREATE TABLE IF NOT EXISTS Votes(
    id SERIAL PRIMARY KEY,
    prompt_id INTEGER,
    user_id INTEGER,
    vote_value VARCHAR(10),
    FOREIGN KEY (prompt_id) REFERENCES Prompts(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
