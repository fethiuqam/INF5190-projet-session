-- CREATE TABLE IF NOT EXISTS arrondissement (
--   id INTEGER PRIMARY KEY,
--   nom VARCHAR(40) NOT NULL UNIQUE
-- );

CREATE TABLE IF NOT EXISTS glissade (
  id INTEGER PRIMARY KEY ,
  nom VARCHAR(40) NOT NULL,
  arrondissement VARCHAR(40) NOT NULL,
  ouvert BOOLEAN ,
  deblaye BOOLEAN ,
  condition VARCHAR(40),
  mise_a_jour DATE
--   FOREIGN KEY (arrondissement_id) REFERENCES arrondissement
);

CREATE TABLE IF NOT EXISTS patinoire (
  id INTEGER PRIMARY KEY ,
  nom VARCHAR(40) NOT NULL,
  arrondissement VARCHAR(40) NOT NULL,
  ouvert BOOLEAN ,
  deblaye BOOLEAN ,
  arrose BOOLEAN,
  resurface BOOLEAN,
  mise_a_jour DATE
--   arrondissement_id INTEGER
--   FOREIGN KEY (arrondissement_id) REFERENCES arrondissement
);

CREATE TABLE IF NOT EXISTS installation_eau (
  id INTEGER PRIMARY KEY ,
  nom VARCHAR(40) NOT NULL,
  arrondissement VARCHAR(40) NOT NULL,
  id_uev INTEGER,
  type_ VARCHAR(20),
  adresse VARCHAR(60),
  propriete VARCHAR(20),
  gestion VARCHAR(20),
  equipement VARCHAR(20),
  point_x REAL,
  point_y REAL,
  longitude REAL,
  latitude REAL
--   arrondissement_id INTEGER
--   FOREIGN KEY (arrondissement_id) REFERENCES arrondissement
);
