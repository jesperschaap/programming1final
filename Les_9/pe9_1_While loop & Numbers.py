som = 0;
aantal = 0;
getal = 1;

while getal != 0:
    getal = int(input("Geef een getal: "));

    som += getal;
    aantal += 1;

print("Er zijn " + str(aantal) + " getallen ingevoerd, de som is: " + str(som));