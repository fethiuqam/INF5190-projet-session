from flask_marshmallow import Marshmallow

ma = Marshmallow()


class InstallationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'type', 'arrondissement', 'condition', 'ouvert',
                  'deblaye', 'mise_a_jour', 'arrose', 'resurface', 'id_uev',
                  'type_piscine', 'adresse', 'propriete', 'gestion',
                  'equipement', 'point_x', 'point_y', 'longitude', 'latitude')


installation_schema = InstallationSchema()
installations_schema = InstallationSchema(many=True)


class GlissadeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'arrondissement', 'ouvert', 'deblaye',
                  'condition', 'mise_a_jour')


glissade_schema = GlissadeSchema()


class PatinoireSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'arrondissement', 'ouvert', 'deblaye',
                  'arrose', 'resurface', 'mise_a_jour')


patinoire_schema = GlissadeSchema()


class PiscineSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'arrondissement', 'id_uev', 'type_piscine',
                  'adresse', 'propriete', 'gestion', 'equipement', 'point_x',
                  'point_y', 'longitude', 'latitude')


piscine_schema = PiscineSchema()

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
            'type': 'string'
        }
    },
    'additionalProperties': False
}

patinoire_update_schema = {
    'type': 'object',
    'required': ['nom', 'arrondissement', 'ouvert', 'deblaye',
                 'arrose', 'resurface', 'mise_a_jour'],
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
        'arrose': {
            'type': ['boolean', 'null']
        },
        'resurface': {
            'type': ['boolean', 'null']
        },
        'mise_a_jour': {
            'type': 'string',
        }
    },
    'additionalProperties': False
}

piscine_update_schema = {
    'type': 'object',
    'required': ['nom', 'arrondissement', 'id_uev', 'type_piscine', 'adresse',
                 'propriete', 'gestion', 'equipement', 'point_x', 'point_y',
                 'longitude', 'latitude'],
    'properties': {
        'nom': {
            'type': 'string'
        },
        'arrondissement': {
            'type': 'string'
        },
        'id_uev': {
            'type': ['number', 'null']
        },
        'type_piscine': {
            'type': 'string'
        },
        'adresse': {
            'type': ['string', 'null']
        },
        'propriete': {
            'type': ['string', 'null']
        },
        'gestion': {
            'type': ['string', 'null']
        },
        'equipement': {
            'type': ['string', 'null']
        },
        'point_x': {
            'type': ['string', 'null']
        },
        'point_y': {
            'type': ['string', 'null']
        },
        'longitude': {
            'type': ['number', 'null']
        },
        'latitude': {
            'type': ['number', 'null']
        }
    },
    'additionalProperties': False
}
