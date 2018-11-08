import requests
import xmltodict

auth_details = ('bas.vandergeer@hotmail.nl', 'YxFPSCscC1zi2BtUZwZ9Cm_ki9FX3x2A_wBTk8xN1MmjKsBKwDv8uw')

# station = input("Vertrekstation: ")
station = str('Gouda')

api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station
response = requests.get(api_url, auth=auth_details)


vertrekXML = xmltodict.parse(response.text)


def request():
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein'][:5]:
                eindbestemming = vertrek['EindBestemming']#Eindbestemming
                typetrein = vertrek['TreinSoort']         # Type Trein
                spoor = vertrek['VertrekSpoor']['#text']  # Spoor in teksts
                vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
                vertrektijd = vertrektijd[11:16]          # 18:36
                print('Om ' + vertrektijd + ' vertrekt vanaf spoor ' + spoor + ' een ' + typetrein + ' naar ' + eindbestemming)

# request()

