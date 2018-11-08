from tkinter import *
import requests
import xmltodict

auth_details = ('bas.vandergeer@hotmail.nl', 'YxFPSCscC1zi2BtUZwZ9Cm_ki9FX3x2A_wBTk8xN1MmjKsBKwDv8uw')
api_url = 'http://webservices.ns.nl/ns-api-avt?station='

def find():
    station = station_entry.get()

    response = requests.get(api_url + station, auth=auth_details)
    xml = xmltodict.parse(response.text)
    for train in xml['ActueleVertrekTijden']['VertrekkendeTrein'][:5]:
        vertrektijd = train['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]
        type = train['TreinSoort']
        spoor = train['VertrekSpoor']['#text']  # Spoor in teksts
        label = Label(master=bottomframe, text= 'Een ' + type + ' naar ' + train['EindBestemming']+ ' vertrekt om ' + vertrektijd + ' vanaf spoor ' + spoor)
        label.pack(fil=X)

root = Tk()

topframe = Frame(master=root)
topframe.pack(side=TOP)

station_entry = Entry(master=topframe)
station_entry.pack(side=LEFT)

station_button = Button(master=topframe, text='Zoek', command=find)
station_button.pack(side=RIGHT)

bottomframe = Frame(master=root)
bottomframe.pack(side=BOTTOM)

root.mainloop()