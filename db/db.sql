
CREATE TABLE IF NOT EXISTS installation (
    id INTEGER PRIMARY KEY ,
    nom VARCHAR(40) NOT NULL,
    arrondissement VARCHAR(40) NOT NULL,
    type VARCHAR (30) NOT NULL,
    condition VARCHAR(40),
    ouvert BOOLEAN ,
    deblaye BOOLEAN ,
    mise_a_jour DATETIME,
    arrose BOOLEAN,
    resurface BOOLEAN,
    id_uev INTEGER,
    type_piscine VARCHAR (30),
    adresse VARCHAR (60),
    propriete VARCHAR (20),
    gestion VARCHAR (20),
    equipement VARCHAR (20),
    point_x VARCHAR (20),
    point_y VARCHAR (20),
    longitude FLOAT,
    latitude FLOAT
);