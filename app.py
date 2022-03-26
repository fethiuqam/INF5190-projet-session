from flask import Flask
from planification import demarrer_planification
from models import *
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/doc')
def documentation():
    gliss = Glissade(nom='nom glissade', arrondissement='arrondissemmmm',
                     ouvert=True, deblaye=False, condition='mauvaise',
                     mise_a_jour=datetime.datetime.now())
    db.session.add(gliss)
    db.session.commit()
    return 'documentation'


demarrer_planification()

with app.app_context():
    db.create_all()

