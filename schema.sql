CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE userlog (id SERIAL PRIMARY KEY, usernameid INTEGER, sent_at TIMESTAMP);
CREATE TABLE liike (id SERIAL PRIMARY KEY, liike TEXT);
CREATE TABLE paikka (id SERIAL PRIMARY KEY, punttisalinNimi TEXT);
CREATE TABLE userStats (id SERIAL PRIMARY KEY, maara INTEGER, painomaara INTEGER, paivamaara TIMESTAMP, liike_id INTEGER REFERENCES liike, users_id INTEGER REFERENCES users, paikka_id INTEGER REFERENCES paikka);
