-- Creation de la table Admin
CREATE TABLE IF NOT EXISTS Admins(
    username VARCHAR(20) UNIQUE NOT NULL PRIMARY KEY,
    firstname VARCHAR(25),
    lastname  VARCHAR(25),
    hashed_password VARCHAR(100)
);

-- Creation de la table UserGroup
CREATE TABLE IF NOT EXISTS Groups(
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(25) UNIQUE NOT NULL,
    admin_info VARCHAR(20),
    FOREIGN KEY (admin_info) REFERENCES Admins(username)
);

-- Creation de la table User
CREATE TABLE IF NOT EXISTS Users(
    username VARCHAR(20) PRIMARY KEY UNIQUE NOT NULL,
    firstname VARCHAR(25),
    lastname  VARCHAR(25),
    hashed_password VARCHAR(100),
    group_id INTEGER,
    admin_info VARCHAR(20),
    FOREIGN KEY (group_id) REFERENCES Groups(id),
    FOREIGN KEY (admin_info) REFERENCES Admins(username)
);

-- Creation de la table Prompt
CREATE TABLE IF NOT EXISTS Prompts(
    id SERIAL PRIMARY KEY,
    prompt_content TEXT,
    price FLOAT DEFAULT 1000,
    note INTEGER CHECK (note >= -10 AND note <= 10) DEFAULT 0,
    status VARCHAR(10) CHECK (status IN ('active', 'pending', 'review', 'reminder', 'delete')) DEFAULT 'pending',
    creat_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_info VARCHAR(20),
    FOREIGN KEY (user_info) REFERENCES Users(username) ON DELETE CASCADE
);

-- Creation de la table Notes
CREATE TABLE IF NOT EXISTS Notes(
    id SERIAL PRIMARY KEY,
    prompt_id  INTEGER,
    user_id INTEGER,
    note_value FLOAT,
    FOREIGN KEY (prompt_id) REFERENCES Prompts(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Creation de la table Votes
CREATE TABLE IF NOT EXISTS Votes(
    id SERIAL PRIMARY KEY,
    prompt_id INTEGER,
    user_id INTEGER,
    vote_value VARCHAR(10),
    FOREIGN KEY (prompt_id) REFERENCES Prompts(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
)