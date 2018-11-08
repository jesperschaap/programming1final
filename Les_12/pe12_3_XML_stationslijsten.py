import xmltodict

def codeandtype():
    file = open("stations.xml", 'rb')
    xml = xmltodict.parse(file)
    print('Dit zijn de codes en types van de 4 stations: ')
    for codeandtype in xml['Stations']['Station']:
        print("{}  \t - {}".format(codeandtype['Code'], codeandtype['Type']))

def synoniem():
    file = open("stations.xml", 'rb')
    xml = xmltodict.parse(file)
    print("")
    print('Dit zijn alle stations met één of meer synoniemen:')
    for synoniem in xml['Stations']['Station']:
        if synoniem['Synoniemen']:
            print("{}  \t - {}".format(synoniem['Code'], synoniem['Synoniemen']))


def longname():
    file = open("stations.xml", 'rb')
    xml = xmltodict.parse(file)
    print("")
    print("Dit is de langste naam van elk station:")
    for station in xml['Stations']['Station']:
        print("{}  \t - {}".format(station['Code'], station['Namen']['Lang']))

def total():
    codeandtype()
    synoniem()
    longname()

total()
