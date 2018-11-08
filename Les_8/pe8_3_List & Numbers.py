invoer = '5-9-7-1-7-8-3-2-4-8-7-9'

def opd(invoer):
    waardes = invoer.split("-");
    getallen = [];
    som = 0;

    for waarde in waardes:
        getallen.append(int(waarde));
        som += int(waarde);

    getallen = sorted(getallen);

    print("Gesorteerde list van ints: " + str(getallen));
    print("Grootste getal: " + str(getallen[-1]) + " en Kleinste getal: " + str(getallen[0]));
    print("Aantal getallen: " + str(len(getallen)) + " en Som van de getallen: " + str(som));
    print("Gemiddelde: " + str(som / len(getallen)));


opd(invoer)