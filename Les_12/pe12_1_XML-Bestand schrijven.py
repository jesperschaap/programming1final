import xmltodict

file = open("index.xml", 'rb')

xml = xmltodict.parse(file)

for artikel in xml['artikelen']['artikel']:
    print(artikel['naam'])