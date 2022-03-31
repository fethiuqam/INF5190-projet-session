from flask_marshmallow import Marshmallow
from models import *
ma = Marshmallow()


class InstallationSchema(ma.Schema):
    class Meta:
        fields = (
            'nom', 'type', 'arrondissement', 'condition', 'ouvert', 'deblaye',
            'mise_a_jour', 'arrose', 'resurface', 'id_uev', 'type_piscine',
            'adresse', 'propriete', 'gestion', 'equipement', 'point_x',
            'point_y', 'longitude', 'latitude')


installation_schema = InstallationSchema()
installations_schema = InstallationSchema(many=True)


class GlissadeSchema(ma.Schema):
    class Meta:
        model = Glissade
        fields = ('id', 'nom', 'arrondissement', 'ouvert', 'deblaye',
                  'condition', 'mise_a_jour')


glissade_schema = GlissadeSchema()
glissades_schema = GlissadeSchema(many=True)

# json-schema

glissade_update_schema = {
    'type': 'object',
    'required': ['nom', 'arrondissement', 'ouvert', 'deblaye',
                 'condition', 'mise_a_jour'],
    'properties': {
        'nom': {
            'type': 'string'
        },
        'arrondissement': {
            'type': 'string'
        },
        'ouvert': {
            'type': ['boolean', 'null']
        },
        'deblaye': {
            'type': ['boolean', 'null']
        },
        'condition': {
            'type': ['string', 'null']
        },
        'mise_a_jour': {
            'type': 'string',
            'format': 'date'
        }
    },
    'additionalProperties': False
}
