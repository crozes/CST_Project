#174794343511-p7h4vpdfebh0h992hoqat80shsolh029.apps.googleusercontent.com
#ABlzb89eGaZHLgiYLNZnQYRW

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import json
import os

from flask import Flask
app = Flask(__name__)



# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

@app.route('/')
def Welcome():
    return "Hello World !"
    
    
@app.route('/sheetID/<string :post_id>')
def getSheetInfo(post_id):
    # Call the Sheets API
    #1vS3-iv0GOnHQTNMudK9yjl-KYdMQZjb7smJ6CNUa4x8
    SPREADSHEET_ID = post_id
    #NomDeLaFeuille!Range1:RangeTop
    RANGE_NAME = 'Feuil1!A2:J'
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
    else:
        #print('Nom, mail:')
        try :
            for row in values:
                horodateur = row[0]
                nom = row[1].upper()
                prenom = row[2].upper()
                sexe = row[3]
                mail = row[4]
                dateNaissance = row[5]
                lieuNaissance = row[6]
                adresse = row[7]
                adresse2 = ''
                if row[8] != NULL :
                    adresse2 = row[8].upper()
                codePostal = row[9]
                ville = row[10]  
                telephone = row[11]
                commentaire = ''
                if row[12] != NULL :
                    commentaire = row[12]
                activite = 'secourisme'    
                result = {'Horodateur':horodateur,'Nom':nom,'Prenom':prenom,'Sexe':sexe,'Mail':mail,'DateNaissance':dateNaissance,'LieuNaissance':lieuNaissance,'Adresse':adresse,'Adresse2':adresse2,'CodePostal':codePostal,'Ville':ville,'Telephone':telephone,'Activite':activite}
                resultFin.append(result)
                #print('%s, %s' % (row[0], row[4]))
        except:
            print("Fin de valeurs")

        print(resultFin)
        return json.dumps(resultFin)
    
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))    