stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"];

def inlezen_station(prompt, stations):
    while True:
        station = input(prompt)

        if station in stations:
            return station

        print("Het opgegeven station bestaat niet")

def inlezen_beginstation(stations):
    return inlezen_station("Geef een begin station: ", stations)

def inlezen_eindstation(stations, beginstation):
    while True:
        station = inlezen_station("Geef een eind station: ", stations)

        if stations.index(station) > stations.index(beginstation):
            return station

        print("Het eindstation moet na het begin station komen")

def omroepen_reis(stations, beginstation, eindstation):
    begin = stations.index(beginstation);
    end = stations.index(eindstation);

    print("Het beginstation " + beginstation + " is het " + str(begin + 1) + "e station in het traject.")
    print("Het eindstation " + eindstation + " is het " + str(end + 1) + "e station in het traject.")
    print("De afstand bedraagt " + str(end - begin) + " station(s).")
    print("De prijs van het kaartje is " + str((end - begin) * 5) + " euro.")
    print("Jij stapt in de trein in: " + beginstation)

    for station in stations[begin + 1:end]:
        print(" - " + station)

    print("Jij stapt uit in: " + eindstation);

beginstation = inlezen_beginstation(stations);
eindstation = inlezen_eindstation(stations, beginstation);
omroepen_reis(stations, beginstation, eindstation)