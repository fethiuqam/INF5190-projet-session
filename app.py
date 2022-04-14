from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError
from models import *
from planification import start_planification
from import_data import import_data
from schemas import *

app = Flask(__name__)
# configuration de l'application selon l'environnement
if app.config["ENV"] == "heroku":
    app.config.from_object("config.HerokuConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevConfig")
else:
    app.config.from_object("config.TestConfig")
# initialisations
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
        installations = Installation.query.filter(
            Installation.arrondissement.ilike(
                f'%{request.args.get("arrondissement")}%')).order_by(
            Installation.nom).all()
    elif request.args.get('nom'):
        installations = Installation.query.filter_by(
            nom=request.args.get('nom')).order_by(
            Installation.nom).all()
    else:
        installations = Installation.query.order_by(
            Installation.nom).all()
    data = installations_schema.dump(installations)
    return jsonify(data)


@app.route('/api/liste-installations/')
def liste_installations():
    installations = db.session.query(Installation).order_by(
        Installation.nom).all()
    data = list(dict.fromkeys([inst.nom for inst in installations]))
    return jsonify(data)


@app.route('/api/glissade/<id>', methods=["PUT"])
@schema.validate(glissade_update_schema)
def modify_glissade(id):
    glissade = Glissade.query.get_or_404(id)
    data = request.get_json()
    new_glissade = Glissade(**data)
    glissade.update(new_glissade)
    db.session.commit()
    return glissade_schema.dump(glissade)


@app.route('/api/glissade/<id>', methods=["DELETE"])
def delete_glissade(id):
    glissade = Glissade.query.get_or_404(id)
    db.session.delete(glissade)
    db.session.commit()
    return "", 200


@app.route('/api/patinoire/<id>', methods=["PUT"])
@schema.validate(patinoire_update_schema)
def modify_patinoire(id):
    patinoire = Patinoire.query.get_or_404(id)
    data = request.get_json()
    new_patinoire = Patinoire(**data)
    patinoire.update(new_patinoire)
    db.session.commit()
    return patinoire_schema.dump(patinoire)


@app.route('/api/patinoire/<id>', methods=["DELETE"])
def delete_patinoire(id):
    patinoire = Patinoire.query.get_or_404(id)
    db.session.delete(patinoire)
    db.session.commit()
    return "", 200


@app.route('/api/piscine/<id>', methods=["PUT"])
@schema.validate(piscine_update_schema)
def modify_piscine(id):
    piscine = Piscine.query.get_or_404(id)
    data = request.get_json()
    new_piscine = Piscine(**data)
    piscine.update(new_piscine)
    db.session.commit()
    return piscine_schema.dump(piscine)


@app.route('/api/piscine/<id>', methods=["DELETE"])
def delete_piscine(id):
    piscine = Piscine.query.get_or_404(id)
    db.session.delete(piscine)
    db.session.commit()
    return "", 200


with app.app_context():
    db.drop_all()
    db.create_all()
    import_data()
    start_planification()
