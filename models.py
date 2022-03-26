from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declared_attr


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


# class InstallationHiver(Installation):
#     ouvert = db.Column(db.Boolean)
#     deblaye = db.Column(db.Boolean)
#     mise_a_jour = db.Column(db.DateTime)
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'installation_hiver'
#     }


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
        return Installation.__table__.c.get('mise_a_jour', db.Column(db.DateTime))


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
        return Installation.__table__.c.get('mise_a_jour', db.Column(db.DateTime))


class Piscine(Installation):
    id_uev = db.Column(db.Integer)
    type_ = db.Column(db.String(30))
    adresse = db.Column(db.String(60))
    propriete = db.Column(db.String(20))
    gestion = db.Column(db.String(20))
    equipement = db.Column(db.String(20))
    point_x = db.Column(db.Float)
    point_y = db.Column(db.Float)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    __mapper_args__ = {
        'polymorphic_identity': 'piscine'
    }
