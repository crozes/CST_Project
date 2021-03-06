# -*- coding: utf-8 -*

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import json
import os

from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)

#A tester
cors = CORS(app)

#--------------------_Function_--------------

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('/home/pi/Serveur/credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('/home/pi/Serveur/client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

@app.route('/')
def Welcome():
    return "Hello World !"
    
@app.route('/sheetID/<post_id>')
def getSheetInfo(post_id):
    # Call the Sheets API
    #1vS3-iv0GOnHQTNMudK9yjl-KYdMQZjb7smJ6CNUa4x8
    SPREADSHEET_ID = post_id
    #NomDeLaFeuille!Range1:RangeTop
    RANGE_NAME = 'Réponses au formulaire 1!A2:P'
    try :
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    except Exception as e:
        print("Erreur")
        print(e)
                                                    
    values = result.get('values', [])

    resultFin = []

    if not values:
        print('No data found.')
        return ''
    else:
        print(values)
        print("------")
        for row in values:
            print(row)
            horodateur = row[0]
            nom = row[1].upper()
            prenom = row[2].upper()
            nationalite = row[3]
            dateNaissance = row[4]
            lieuNaissance = row[5]
            departement = row[6]
            sexe = row[7]
            adresse = row[8]
            adresse2 = ''
            if row[9] != "" :
                adresse2 = row[9]
            codePostal = row[10]
            ville = row[11]
            pays = row[12]
            telephone = ''
            if row[13] != "" :
                telephone = '0'+row[13]
            portable = ''
            if row[14] != "" :    
                portable = '0'+row[14]
            mail = row[15]
            commentaire = ''
            #if row[16] != None :
            #    commentaire = row[16]
            activite = 'secourisme'    
            result = {'Horodateur':horodateur,'Nom':nom,'Prenom':prenom,'Nationalite':nationalite,'Portable':portable,'Departement':departement,'Pays':pays,'Sexe':sexe,'Mail':mail,'DateNaissance':dateNaissance,'LieuNaissance':lieuNaissance,'Adresse':adresse,'Adresse2':adresse2,'CodePostal':codePostal,'Ville':ville,'Telephone':telephone,'Activite':activite}
            resultFin.append(result)
                
        print(resultFin)
        print("-----")
        return jsonify(resultFin)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
