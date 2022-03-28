from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

from planification import demarrer_planification
from models import *
from import_donnees import importer_donnees
from schemas import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)


@app.route('/doc')
def documentation():
    return render_template('doc.html')


@app.route('/api/installations/')
def installations():
    if request.args.get('arrondissement'):
        installations = Installation.query.filter_by(
            arrondissement=request.args.get('arrondissement'))
    else:
        installations = Installation.query.all()
    data = set([installation.nom for installation in installations])
    return jsonify(list(data))


@app.route('/api/liste_installations/')
def liste_installations():
    installations = db.session.query(Installation).order_by(
        Installation.nom).all()
    data = installations_schema.dump(installations)
    return jsonify(data)


with app.app_context():
    db.create_all()
    importer_donnees()
    demarrer_planification()
