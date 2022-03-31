from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError

from planification import demarrer_planification
from models import *
from import_donnees import importer_donnees
from schemas import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)
schema = JsonSchema(app)


@app.errorhandler(JsonValidationError)
def validation_error(e):
    errors = [validation_error.message for validation_error in e.errors]
    return jsonify({'error': e.message, 'errors': errors}), 400


@app.route('/')
def index():
    return render_template('index.html')


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


@app.route('/api/glissade/<id>', methods=["PUT"])
@schema.validate(glissade_update_schema)
def modify_glissade(id):
    glissade = Glissade.query. get_or_404(id)
    data = request.get_json()
    new_glissade = Glissade(**data)
    glissade.update(new_glissade)
    db.session.commit()
    return glissade_schema.dump(glissade)


@app.route('/api/glissade/<id>', methods=["DELETE"])
def delete_glissade(id):
    glissade = Glissade.query. get_or_404(id)
    db.session.delete(glissade)
    db.session.commit()
    return "", 200


with app.app_context():
    db.create_all()
    importer_donnees()
    demarrer_planification()
