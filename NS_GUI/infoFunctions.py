import requests
import xmltodict
from tkinter import messagebox



def getStationInfo(stationName):
    error_message = ''
    auth_details = ('bas.vandergeer@hotmail.nl', 'YxFPSCscC1zi2BtUZwZ9Cm_ki9FX3x2A_wBTk8xN1MmjKsBKwDv8uw')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + stationName

    try:
        response = requests.get(api_url, auth=auth_details)
    except requests.ConnectionError:
        messagebox.showerror("Error", 'Geen verbinding')
        exit()

    vertrekXML = xmltodict.parse(response.text)

    if 'error' in vertrekXML:
        messagebox.showerror("Error", vertrekXML['error']['message'])


    return vertrekXML


def data(stationName):
    dataXML = getStationInfo(stationName)
    data = []
    #print(dataXML)


    if 'error' not in dataXML:
        for vertrek in dataXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']
            vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
            vertrektijd = vertrektijd[11:16]  # 18:36


            try:
                spoor = vertrek['VertrekSpoor']['#text']
                trein_soort = vertrek['TreinSoort']

            except KeyError:
                spoor = 'Spoor niet beschikbaar'
                trein_soort = 'trein'





            data += ['Om ' + vertrektijd + ' vertrekt een ' + trein_soort + ' naar ' + eindbestemming + ' op spoor: ' + spoor]
            # print(data)

    return data

# data('Utrecht')
