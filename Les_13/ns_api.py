import requests
import xmltodict

auth_details = ('bas.vandergeer@hotmail.nl', 'YxFPSCscC1zi2BtUZwZ9Cm_ki9FX3x2A_wBTk8xN1MmjKsBKwDv8uw')

station = input("Vertrekstation: ")

api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station
response = requests.get(api_url, auth=auth_details)


vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']
    typetrein = vertrek['TreinSoort']
    spoor = vertrek['VertrekSpoor']['#text']
    vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]          # 18:36

    print('Om '+vertrektijd+ ' vertrekt vanaf spoor ' + spoor + ' een ' + typetrein + ' naar '+ eindbestemming)