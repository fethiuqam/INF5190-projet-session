from flask import Flask
from planification import demarrer_planification
from models import *
from import_donnees import importer_donnees


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/doc')
def documentation():

    return 'documentation'


with app.app_context():
    importer_donnees()
    demarrer_planification()

