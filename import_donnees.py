import pandas as pd
import requests
import xml.etree.ElementTree as ET
import sqlite3

url_installation_eau = 'https://data.montreal.ca/dataset/4604afb7-a7c4-4626-' \
                       'a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-' \
                       '9af73af03b14/download/piscines.csv'
url_patinoire = 'https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-' \
                'a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0' \
                '/download/l29-patinoire.xml'
url_glissade = 'http://www2.ville.montreal.qc.ca/services_citoyens/' \
               'pdf_transfert/L29_GLISSADE.xml'


def importer_donnees():
    connection = sqlite3.connect('db/sqlite.db')

    # supprimer la base de donnees
    connection.execute("delete from installation_eau")
    connection.execute("delete from glissade")
    connection.execute("delete from patinoire")
    connection.commit()

    # importation des donnees des installations d'eau
    data_installation_eau = pd.read_csv(url_installation_eau, na_filter=False)
    for index, row in data_installation_eau.iterrows():
        connection.execute((
            "insert into installation_eau (id_uev, nom, arrondissement, type_,"
            " adresse, propriete, gestion, equipement, point_x, point_y, "
            "longitude, latitude) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"),
            (row['ID_UEV'], row['NOM'], row['ARRONDISSE'],
             row['TYPE'], row['ADRESSE'], row['PROPRIETE'],
             row['GESTION'], row['EQUIPEME'], row['POINT_X'],
             row['POINT_Y'], row['LONG'], row['LAT']))

    connection.commit()

    # importation des donnees des glissades
    data_glissade = requests.get(url_glissade, allow_redirects=True)
    root_glissade = ET.fromstring(data_glissade.content)
    for glissade in root_glissade:
        nom = glissade[0].text.strip()
        arrondissement = glissade[1][0].text.strip()
        date_maj = glissade[1][2].text.strip()
        ouvert = glissade[2].text
        deblaye = glissade[3].text
        condition = glissade[4].text.strip()
        connection.execute((
            "insert into glissade (nom, arrondissement, ouvert, deblaye, "
            "condition, mise_a_jour) values(?, ?, ?, ?, ?, ?)"),
            (nom, arrondissement, ouvert, deblaye, condition, date_maj))

    connection.commit()

    # importation des donnees des patinoires
    data_patinoire = requests.get(url_patinoire, allow_redirects=True)
    root_patinoire = ET.fromstring(data_patinoire.content)
    for arr in root_patinoire:
        arrondissement = arr[0].text.strip()
        nom = arr[1][0].text.strip()
        date_maj = arr[1][-1][0].text.strip()
        ouvert = arr[1][-1][1].text
        deblaye = arr[1][-1][2].text
        arrose = arr[1][-1][3].text
        resurface = arr[1][-1][4].text
        connection.execute((
            "insert into patinoire (nom, arrondissement, ouvert, deblaye, "
            "arrose, resurface, mise_a_jour) values(?, ?, ?, ?, ?, ?, ?)"), (
            nom, arrondissement, ouvert, deblaye, arrose, resurface, date_maj))

    connection.commit()

    connection.close()

    print('Fin de l import des données')