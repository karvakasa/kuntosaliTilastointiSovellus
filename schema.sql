CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE userlog (id SERIAL PRIMARY KEY, usernameid INTEGER, sent_at TIMESTAMP);
