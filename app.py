from flask import Flask

app = Flask(__name__)


@app.route('/doc')
def documentation():
    return 'documentation'
