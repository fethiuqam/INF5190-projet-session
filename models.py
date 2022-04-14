from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declared_attr
from datetime import datetime

db = SQLAlchemy()


class Installation(db.Model):
    __tablename__ = 'installation'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(40), nullable=False)
    arrondissement = db.Column(db.String(40), nullable=False)
    type = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'installation'
    }


class Glissade(Installation):
    condition = db.Column(db.String(40))

    __mapper_args__ = {
        'polymorphic_identity': 'glissade'
    }

    @declared_attr
    def ouvert(cls):
        return Installation.__table__.c.get('ouvert', db.Column(db.Boolean))

    @declared_attr
    def deblaye(cls):
        return Installation.__table__.c.get('deblaye', db.Column(db.Boolean))

    @declared_attr
    def mise_a_jour(cls):
        return Installation.__table__.c.get('mise_a_jour',
                                            db.Column(db.DateTime))

    def __init__(self, nom, arrondissement, ouvert, deblaye, condition,
                 mise_a_jour):
        self.nom = nom
        self.arrondissement = arrondissement
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.condition = condition
        self.mise_a_jour = string_to_datetime(mise_a_jour)

    def update(self, other):
        self.nom = other.nom
        self.arrondissement = other.arrondissement
        self.ouvert = other.ouvert
        self.deblaye = other.deblaye
        self.condition = other.condition
        self.mise_a_jour = other.mise_a_jour


class Patinoire(Installation):
    arrose = db.Column(db.Boolean)
    resurface = db.Column(db.Boolean)

    __mapper_args__ = {
        'polymorphic_identity': 'patinoire'
    }

    @declared_attr
    def ouvert(cls):
        return Installation.__table__.c.get('ouvert', db.Column(db.Boolean))

    @declared_attr
    def deblaye(cls):
        return Installation.__table__.c.get('deblaye', db.Column(db.Boolean))

    @declared_attr
    def mise_a_jour(cls):
        return Installation.__table__.c.get('mise_a_jour',
                                            db.Column(db.DateTime))

    def __init__(self, nom, arrondissement, ouvert, deblaye, arrose, resurface,
                 mise_a_jour):
        self.nom = nom
        self.arrondissement = arrondissement
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.arrose = arrose
        self.resurface = resurface
        self.mise_a_jour = string_to_datetime(mise_a_jour)

    def update(self, other):
        self.nom = other.nom
        self.arrondissement = other.arrondissement
        self.ouvert = other.ouvert
        self.deblaye = other.deblaye
        self.arrose = other.arrose
        self.resurface = other.resurface
        self.mise_a_jour = other.mise_a_jour


class Piscine(Installation):
    id_uev = db.Column(db.Integer)
    type_piscine = db.Column(db.String(30))
    adresse = db.Column(db.String(60))
    propriete = db.Column(db.String(20))
    gestion = db.Column(db.String(20))
    equipement = db.Column(db.String(20))
    point_x = db.Column(db.String(20))
    point_y = db.Column(db.String(20))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    __mapper_args__ = {
        'polymorphic_identity': 'piscine'
    }

    def __init__(self, nom, arrondissement, id_uev, type_piscine, adresse,
                 propriete, gestion, equipement, point_x, point_y, longitude,
                 latitude):
        self.nom = nom
        self.arrondissement = arrondissement
        self.id_uev = id_uev
        self.type_piscine = type_piscine
        self.adresse = adresse
        self.propriete = propriete
        self.gestion = gestion
        self.equipement = equipement
        self.point_x = point_x
        self.point_y = point_y
        self.longitude = longitude
        self.latitude = latitude

    def update(self, other):
        self.nom = other.nom
        self.arrondissement = other.arrondissement
        self.type_piscine = other.type_piscine
        self.id_uev = other.id_uev
        self.adresse = other.adresse
        self.propriete = other.propriete
        self.gestion = other.gestion
        self.equipement = other.equipement
        self.point_x = other.point_x
        self.point_y = other.point_y
        self.longitude = other.longitude
        self.latitude = other.latitude


def string_to_datetime(chaine):
    if chaine:
        try:
            return datetime.fromisoformat(chaine)
        except ValueError as err:
            print("Erreur : Le format de la date ne respecte pas la forme "
                  "ISO 8601")
    return None
