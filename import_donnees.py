import pandas as pd
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

from models import *

# import sqlite3

url_installation_eau = 'https://data.montreal.ca/dataset/4604afb7-a7c4-4626-' \
                       'a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-' \
                       '9af73af03b14/download/piscines.csv'
url_patinoire = 'https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-' \
                'a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0' \
                '/download/l29-patinoire.xml'
url_glissade = 'http://www2.ville.montreal.qc.ca/services_citoyens/' \
               'pdf_transfert/L29_GLISSADE.xml'


def importer_donnees():
    #connection = sqlite3.connect('db/sqlite.db')
    #
    # # supprimer la base de donnees
    # connection.execute("delete from installation_eau")
    # connection.execute("delete from glissade")
    # connection.execute("delete from patinoire")
    # connection.commit()
    db.drop_all()
    db.create_all()


    # importation des donnees des installations d'eau
    data_piscine = pd.read_csv(url_installation_eau, na_filter=False)
    for index, row in data_piscine.iterrows():
        piscine = Piscine(nom=row['NOM'], arrondissement=row['ARRONDISSE'],
                          id_uev=row['ID_UEV'], type_piscine=row['TYPE'],
                          adresse=row['ADRESSE'], propriete=row['PROPRIETE'],
                          gestion=row['GESTION'], equipement=row['EQUIPEME'],
                          point_x=row['POINT_X'], point_y=row['POINT_Y'],
                          longitude=row['LONG'], latitude=row['LAT'])
        db.session.add(piscine)
    db.session.commit()

        # connection.execute((
        #     "insert into installation_eau (id_uev, nom, arrondissement, type_,"
        #     " adresse, propriete, gestion, equipement, point_x, point_y, "
        #     "longitude, latitude) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"),
        #     (row['ID_UEV'], row['NOM'], row['ARRONDISSE'],
        #      row['TYPE'], row['ADRESSE'], row['PROPRIETE'],
        #      row['GESTION'], row['EQUIPEME'], row['POINT_X'],
        #      row['POINT_Y'], row['LONG'], row['LAT']))
    #connection.commit()

    # importation des donnees des glissades
    data_glissade = requests.get(url_glissade, allow_redirects=True)
    root_glissade = ET.fromstring(data_glissade.content)
    for elem_glissade in root_glissade:
        nom = elem_glissade[0].text.strip()
        arrondissement = elem_glissade[1][0].text.strip()
        date_maj = string_to_datetime(elem_glissade[1][2].text)
        ouvert = string_to_boolean(elem_glissade[2].text)
        deblaye = string_to_boolean(elem_glissade[3].text)
        condition = elem_glissade[4].text.strip()
        glissade = Glissade(nom=nom, arrondissement=arrondissement,
                            ouvert=ouvert, deblaye=deblaye,
                            condition=condition, mise_a_jour=date_maj)
        db.session.add(glissade)
    db.session.commit()


    #     connection.execute((
    #         "insert into glissade (nom, arrondissement, ouvert, deblaye, "
    #         "condition, mise_a_jour) values(?, ?, ?, ?, ?, ?)"),
    #         (nom, arrondissement, ouvert, deblaye, condition, date_maj))
    # connection.commit()

    # importation des donnees des patinoires
    data_patinoire = requests.get(url_patinoire, allow_redirects=True)
    root_patinoire = ET.fromstring(data_patinoire.content)
    for arr in root_patinoire:
        arrondissement = arr[0].text.strip()
        nom = arr[1][0].text.strip()
        date_maj = string_to_datetime(arr[1][-1][0].text.strip())
        ouvert = string_to_boolean(arr[1][-1][1].text)
        deblaye = string_to_boolean(arr[1][-1][2].text)
        arrose = string_to_boolean(arr[1][-1][3].text)
        resurface = string_to_boolean(arr[1][-1][4].text)
        patinoire = Patinoire(nom=nom, arrondissement=arrondissement,
                              ouvert=ouvert, deblaye=deblaye, arrose=arrose,
                              resurface=resurface, mise_a_jour=date_maj)
        db.session.add(patinoire)
    db.session.commit()

    #     connection.execute((
    #         "insert into patinoire (nom, arrondissement, ouvert, deblaye, "
    #         "arrose, resurface, mise_a_jour) values(?, ?, ?, ?, ?, ?, ?)"), (
    #         nom, arrondissement, ouvert, deblaye, arrose, resurface, date_maj))
    #
    # connection.commit()
    #
    # connection.close()

    print('Fin de l import des données')


def string_to_boolean(chaine):
    if chaine:
        chaine = chaine.strip()
    else:
        return None
    if chaine == '0':
        return False
    elif chaine == '1':
        return True
    else:
        return None


def string_to_datetime(chaine):
    if chaine:
        return datetime.strptime(chaine, '%Y-%m-%d %H:%M:%S')
    else:
        return None
