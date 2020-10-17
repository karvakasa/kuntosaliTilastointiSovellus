CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE userlog (id SERIAL PRIMARY KEY, usernameid INTEGER REFERENCES users, sent_at TIMESTAMP);
CREATE TABLE equipment (id SERIAL PRIMARY KEY, gym_equipment TEXT);
CREATE TABLE gym (id SERIAL PRIMARY KEY, gym_place TEXT);
CREATE TABLE userStats (id SERIAL PRIMARY KEY, do_amount INTEGER, weight_amount INTEGER, date TIMESTAMP,
 equipment_id INTEGER REFERENCES equipment, users_id INTEGER REFERENCES users, gym_id INTEGER REFERENCES gym);

INSERT INTO equipment (gym_equipment) VALUES ('bench_press');
INSERT INTO equipment (gym_equipment) VALUES ('scottish_bench');
INSERT INTO equipment (gym_equipment) VALUES ('squat');
INSERT INTO equipment (gym_equipment) VALUES ('foot_press');
INSERT INTO equipment (gym_equipment) VALUES ('deadlift');

INSERT INTO gym (gym_place) VALUES ('Unisport');
INSERT INTO gym (gym_place) VALUES ('Elixia');
INSERT INTO gym (gym_place) VALUES ('Fressi');
INSERT INTO gym (gym_place) VALUES ('fitness24/7');
INSERT INTO gym (gym_place) VALUES ('Fit');
INSERT INTO gym (gym_place) VALUES ('EasyFit');