from flask import Flask
from planification import demarrer_planification

app = Flask(__name__)


@app.route('/doc')
def documentation():
    return 'documentation'


demarrer_planification()
