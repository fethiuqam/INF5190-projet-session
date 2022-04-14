
CREATE TABLE IF NOT EXISTS installation (
    id INTEGER PRIMARY KEY ,
    nom VARCHAR(100) NOT NULL,
    arrondissement VARCHAR(100) NOT NULL,
    type VARCHAR (30) NOT NULL,
    condition VARCHAR(100),
    ouvert BOOLEAN ,
    deblaye BOOLEAN ,
    mise_a_jour DATETIME,
    arrose BOOLEAN,
    resurface BOOLEAN,
    id_uev INTEGER,
    type_piscine VARCHAR (100),
    adresse VARCHAR (100),
    propriete VARCHAR (100),
    gestion VARCHAR (100),
    equipement VARCHAR (100),
    point_x VARCHAR (30),
    point_y VARCHAR (30),
    longitude FLOAT,
    latitude FLOAT
);