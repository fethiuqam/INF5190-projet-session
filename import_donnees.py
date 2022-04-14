import pandas as pd
import requests
import xml.etree.ElementTree as ET
from models import *

url_piscine = 'https://data.montreal.ca/dataset/4604afb7-a7c4-4626-' \
              'a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-' \
              '9af73af03b14/download/piscines.csv'
url_patinoire = 'https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-' \
                'a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0' \
                '/download/l29-patinoire.xml'
url_glissade = 'http://www2.ville.montreal.qc.ca/services_citoyens/' \
               'pdf_transfert/L29_GLISSADE.xml'


def importer_donnees():
    # importation des donnees des piscines
    data_piscine = pd.read_csv(url_piscine, na_filter=False)
    for index, row in data_piscine.iterrows():
        new_piscine = Piscine(row['NOM'], row['ARRONDISSE'], row['ID_UEV'],
                              row['TYPE'], row['ADRESSE'], row['PROPRIETE'],
                              row['GESTION'], row['EQUIPEME'], row['POINT_X'],
                              row['POINT_Y'], row['LONG'], row['LAT'])
        piscine = Piscine.query.filter_by(nom=new_piscine.nom,
                        type_piscine=new_piscine.type_piscine).first()
        update_data(piscine, new_piscine)

    # importation des donnees des glissades
    data_glissade = requests.get(url_glissade, allow_redirects=True)
    root_glissade = ET.fromstring(data_glissade.content)
    for elem_glissade in root_glissade:
        nom = elem_glissade[0].text.strip()
        arrondissement = elem_glissade[1][0].text.strip()
        date_maj = elem_glissade[1][2].text.strip()
        ouvert = string_to_boolean(elem_glissade[2].text)
        deblaye = string_to_boolean(elem_glissade[3].text)
        condition = elem_glissade[4].text.strip()
        new_glissade = Glissade(nom, arrondissement, ouvert, deblaye,
                                condition, date_maj)
        glissade = Glissade.query.filter_by(nom=new_glissade.nom).first()
        update_data(glissade, new_glissade)

    # importation des donnees des patinoires
    data_patinoire = requests.get(url_patinoire, allow_redirects=True)
    root_patinoire = ET.fromstring(data_patinoire.content)
    for arr in root_patinoire:
        arrondissement = arr[0].text.strip()
        nom = arr[1][0].text.strip()
        date_maj = arr[1][-1][0].text.strip()
        ouvert = string_to_boolean(arr[1][-1][1].text)
        deblaye = string_to_boolean(arr[1][-1][2].text)
        arrose = string_to_boolean(arr[1][-1][3].text)
        resurface = string_to_boolean(arr[1][-1][4].text)
        new_patinoire = Patinoire(nom, arrondissement, ouvert, deblaye, arrose,
                                  resurface, date_maj)
        patinoire = Patinoire.query.filter_by(nom=new_patinoire.nom).first()
        update_data(patinoire, new_patinoire)

    print('Fin de l import des données')


def update_data(data, new_data):
    if data is None:
        db.session.add(new_data)
        db.session.commit()
    elif data != new_data:
        data.update(new_data)
        db.session.commit()


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
