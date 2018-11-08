import datetime
import csv

bestand = 'inloggers.csv'
file = open(bestand, 'w+')
writer = csv.writer(file)


while True:
    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
        break;

    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    date = datetime.datetime.now()
    writer.writerow([date.strftime('%a %d %b %Y, %X'), naam, voorl, gbdatum, email])
