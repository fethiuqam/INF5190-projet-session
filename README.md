# Projet de session INF5190 - Application REST

Le projet consiste à récupérer un ensemble de données concernant des installations aquatiques et d'activités d'hiver,
provenant de l'api de la ville de Montréal,
puis les rendre disponible via un service web. 

L'utilisateur pourra consulter ces données, les modifier et même les supprimer.

L'application se base sur la téchnologie flask de Python.

Ce travail rentre dans le cadre du projet de session du cours INF5190, Hiver 2022.

## Prérequis

Afin de pouvoir exécuter l'application sur votre poste, vous devez d'abord installer les dépendances suivantes :

* Python 3.7 : https://www.python.org/downloads/release/python-3712/
* Sqlite 3.38 : https://www.sqlite.org/download.html

## Téchnologies :

* Python 3.7
* Flask 2.0.1
* Jinja2 3.0.1
* Sqlite 3.38
* Bootstrap 5.1.3
* JQuery 3.6.0

## installation et activation de l'environnement python

Il faut installer virtualenv par la commande :

```
$ python3 -m pip install virtualenv
```

positionnez vous à la racine du repertoire et créez un environnement virtuel Python par la commande :

```
$ python3 -m venv flask-env
```

Puis activez cet environnement par la commande :

```
$ source flask-env/bin/activate
```

Après l'activation, installez les dependances de l'application par la commande :

```
$ sudo pip install -r requirements.txt
```

## initialisation de la base de données :

Il n'est pas nécessaire d'initialiser la base de données avant de lancer l'application car cette dernière utilise
la bibliothèque SQLAlchemy. L'application crée la base de données à son lancement si elle n'existe pas déjà.

## exécution et lancement de l'application

Après avoir activé l'environnement et installé toutes les dépendances, vous pouvez lancer
l'application par la commande :

```
$ make
```

Une fois l'application lancée, utilisez le fureteur de votre poste pour accéder à l'application Flask. 

Vous pouvez y accéder en utilisant l'adresse URL  `http://127.0.0.1:5000/`

Il faut attendre un laps de temps avant d'accéder à la page d'accueil, car l'application doit télécharger 
et peupler sa base de données à son lancement. Cette étape ce termine par l'affichage du message `Fin de l import des données` sur la console.

## contributeur:

Nom : FETHI BEY ABI AYAD

Code permanent : ABIF10108204

## sources 

Je me suis basé sur quelques sites pour résoudre les problèmes rencontrés durant mon travail : 

- https://docs.sqlalchemy.org/en/14/orm/inheritance.html
- https://stackoverflow.com/questions/22929839/circular-import-of-db-reference-using-flask-sqlalchemy-and-blueprints
- https://flask.palletsprojects.com/en/2.0.x/appcontext/#:~:text=Flask%20automatically%20pushes%20an%20application,cli%20using%20%40app.
- https://careerkarma.com/blog/python-remove-duplicates-from-list/#:~:text=You%20can%20remove%20duplicates%20from,whose%20duplicates%20have%20been%20removed.
- https://stackoverflow.com/questions/29775797/fetch-post-json-data
- https://pythonise.com/series/learning-flask/flask-configuration-files
- https://www.deepanseeralan.com/tech/iso-datetime-conversions-python/
- https://medium.com/analytics-vidhya/server-validation-in-flask-api-with-json-schema-963aa05e305f