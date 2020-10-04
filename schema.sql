CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE userlog (id SERIAL PRIMARY KEY, usernameid INTEGER, sent_at TIMESTAMP);
CREATE TABLE liike (id SERIAL PRIMARY KEY, liike TEXT);
CREATE TABLE paikka (id SERIAL PRIMARY KEY, punttisalinnimi TEXT);
CREATE TABLE userStats (id SERIAL PRIMARY KEY, maara INTEGER, painomaara INTEGER, paivamaara TIMESTAMP, liike_id INTEGER REFERENCES liike, users_id INTEGER REFERENCES users, paikka_id INTEGER REFERENCES paikka);

INSERT INTO liike (liike) VALUES ('Penkki');
INSERT INTO liike (liike) VALUES ('SkottiPenkki');
INSERT INTO liike (liike) VALUES ('Kyykky');
INSERT INTO liike (liike) VALUES ('Jalkaprässi');
INSERT INTO liike (liike) VALUES ('Maastaveto');

INSERT INTO paikka (punttisalinnimi) VALUES ('Unisport');
INSERT INTO paikka (punttisalinnimi) VALUES ('Elixia');
INSERT INTO paikka (punttisalinnimi) VALUES ('Fressi');
INSERT INTO paikka (punttisalinnimi) VALUES ('fitness24/7');
INSERT INTO paikka (punttisalinnimi) VALUES ('Fit');
INSERT INTO paikka (punttisalinnimi) VALUES ('EasyFit');