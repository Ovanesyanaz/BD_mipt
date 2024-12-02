CREATE table USERS (
    user_id INTEGER UNIQUE PRIMARY KEY NOT NULL,
    email TEXT UNIQUE NOT NULL,
    geo TEXT NOT NULL
);

CREATE table LOG (
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    time TEXT NOT NULL PRIMARY KEY,
    bet INTEGER,
    win INTEGER
);
