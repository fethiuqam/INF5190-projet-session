from flask_marshmallow import Marshmallow

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
        fields = ('nom', 'type', 'arrondissement', 'ouvert')


glissade_schema = GlissadeSchema()
glissades_schema = GlissadeSchema(many=True)
