#  Les fonctionnalités implémentées dans le projet de session

## A1 15xp:

Trois listes de données doivent être obtenues à l'aide de requêtes HTTP et leur contenu doit être stocké dans une base de données SQLite.

Cette fonctionnalité est exécutée au lancement de l’application Flask.
L’import de données se termine par l’affichage du message `Fin de l import des données` sur la console.

L’implémentation de cette fonctionnalité est dans le script python `import_data.py`

## A2 5xp:

L'importation de données du point A1 est faite automatiquement chaque jour à minuit à l’aide d’un BackgroundScheduler.

Cette fonctionnalité est lancée au lancement de l’application après le premier import de données.

L’implémentation de cette fonctionnalité est dans le script python `planification.py`

## A3 5xp:

Le système écoute les requêtes HTTP sur le port 5000. La route « /doc » fait apparaître la documentation de tous les services REST. La documentation est en format HTML, généré à partir de fichiers RAML. Intégrez la fonctionnalité du point A2 à l’application Flask créée au point A3.

Cette fonctionnalité est lancée par la commande `make` à la racine du projet. La documentation peut être consultée sur l’url `http://127.0.0.1:5000/doc/`

## A4 10xp:
Le système offre un service REST permettant d'obtenir la liste des installations pour un arrondissement spécifié en paramètre. Les données retournées sont en format JSON. Ex. GET /api/installations?arrondissement=LaSalle

Cette fonctionnalité peut être testée par l’envoi d’une requête `GET` sur l’url `http://127.0.0.1:5000/api/installations` en spécifiant le paramètre de recherche `arrondissement`.
Le résultat retourné consiste en une liste hétérogène d’objet en format JSON dont le nom d’arrondissement inclut le paramètre de la requête.

Exemple de la requête: `http://127.0.0.1:5000/api/installations?arrondissement=LaSalle`

## A5 10xp
Une application JavaScript/HTML permet de saisir un arrondissement à partir d'un formulaire HTML. Lorsque l'utilisateur lance la recherche, une requête asynchrone contenant l'arrondissement saisis est envoyée à la route définie en A4. Lorsque la réponse asynchrone revient, l'application affiche la liste des installations dans un tableau. L'application est disponible sur la page d'accueil du serveur (route « / »).

Cette fonctionnalité peut être testée sur l’url `http://127.0.0.1:5000/` . Cela consiste à entrer un mot clé dans le champs `Rechercher par arrondissement`, par exemple le mot: `lasalle` puis cliquer sur le bouton `Recherche`.
L’application affiche les résultats sous forme d’un tableau en séparant les 3 types d’installations: glissades, patinoires et piscines.

## A6 10xp
L'application du point A5 offre un mode de recherche par nom d'installation. La liste de toutes les installations est prédéterminée dans une liste déroulante et l'utilisateur choisira une installation parmi cette liste. Lorsque l'utilisateur lance la recherche, une requête asynchrone est envoyée à un service REST que vous devez créer à cet effet. Lorsque la réponse asynchrone revient, l'application affiche l'information connue sur cette installation.

Cette fonctionnalité peut être testée sur l’url `http://127.0.0.1:5000/` . Cela consiste sélectionner un nom d’installation  dans la liste déroulante `Rechercher par installation`,  cela affichera les installations portant ce nom. 

L’application front-end javascript envoie une requête `GET` asynchrone sur l’url `http://127.0.0.1:5000/api/installations?nom=<nom d’installation>`

NB: dans le cas des piscines, un seul nom peut correspondre à plusieurs types d’installation.

## C1 10xp:
Le système offre un service REST permettant d'obtenir la liste des installations leur type. Il y a 3 types possibles : glissade, piscine, patinoire (les 3 fichiers de données de départ). Pour chaque installation, on indique toute l'information connue. La liste est triée en ordre croissant du nom de l'installation.

Cette fonctionnalité peut être testée par l’envoi d’une requête `GET` sur l’url `http://127.0.0.1:5000/api/installations` .
Le résultat retourné consiste en une liste hétérogène d’objet en format JSON triés en ordre croissant par  le nom d’installation .

## D1 15xp:
Le système offre un service REST permettant de modifier l'état d'une glissade. Le client doit envoyer un document JSON contenant les modifications à apporter à la glissade. Le document JSON doit être validé avec json-schema.

Cette fonctionnalité peut être testée par l’envoi d’une requête `PUT` sur l’url `http://127.0.0.1:5000/api/glissade/<id>` .
La structure de l’objet à envoyer et le type de retour sont précisés sur la page de documentation `http://127.0.0.1:5000/doc/`.

## D2 5xp:
Le système offre un service REST permettant de supprimer une glissade.

Cette fonctionnalité peut être testée par l’envoi d’une requête `DELETE` sur l’url `http://127.0.0.1:5000/api/glissade/<id>` .

## D3 5xp:
Modifier l'application faite en A5 afin de pouvoir supprimer ou modifier les glissades retournées par l'outil de recherche. L'application doit invoquer les services faits en D1 et D2 avec des appels asynchrones et afficher une confirmation en cas de succès ou un message d'erreur en cas d'erreur. Il faut développer la même fonctionnalité pour les piscines et installations aquatiques.

On a ajouter 4 routes à l’api pour les patinoires et les piscines:
- `PUT` : `http://127.0.0.1:5000/api/patinoire/<id>`
- `DELETE` : `http://127.0.0.1:5000/api/patinoire/<id>`
- `PUT` : `http://127.0.0.1:5000/api/piscine/<id>`
- `DELETE` : `http://127.0.0.1:5000/api/piscine/<id>`

La structure de l’objet à envoyer et le type de retour sont précisés sur la page de documentation `http://127.0.0.1:5000/doc/`.

Les tableaux des résultats de recherche de l’application front-end javascript contiennent en plus pour chaque ligne de résultat les boutons `Modifier` et `Supprimer` pour pouvoir effectuer les modifications et les suppressions.

L’application front-end ne permet pas la modification du nom d’installation et de l’arrondissement ainsi que le type de piscine. Cependant, les requêtes manuelles par `Postman` par exemple le permettent.  

## F1 20xp:
Le système est entièrement déployé sur la plateforme infonuagique Heroku.

L’url de l’application sur la plateforme Heroku est la suivante :
https://montreal-installation-aquatiq.herokuapp.com/

