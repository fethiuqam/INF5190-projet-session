from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

from planification import demarrer_planification
from models import *
from import_donnees import importer_donnees

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/doc')
def documentation():
    return render_template('doc.html')


@app.route('/api/installations/')
def liste_installations():
    installations = None
    if request.args.get('arrondissement'):
        installations = Installation.query.filter_by(
            arrondissement=request.args.get('arrondissement'))
    else:
        installations = Installation.query.all()

    data = [{"nom": inst.nom, "type": inst.type} for inst in installations]
    return jsonify(data)


with app.app_context():
    #importer_donnees()
    demarrer_planification()
