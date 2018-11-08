def namen():
    klas = {}
    while True:
        naam = input("Volgende naam: ")
        if len(naam) == 0:
            break;

        if naam in klas:
            klas[naam] += 1;
        else:
            klas[naam] = 1;

    for naam in klas:
        if klas[naam] == 1:
            print("Er is " + str(klas[naam]) + " student met de naam " + naam);
        else:
            print("Er zijn " + str(klas[naam]) + " studenten met de naam " + naam);

namen()