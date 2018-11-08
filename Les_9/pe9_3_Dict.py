cijfers = {
    "Barthold": 10,
    "Bas": 9.5,
    "Niels": 3,
    "Imme": 5.5,
    "Ziad": 9.5,
    "Lucas": 6,
    "Patrick": 2,
    "Reza": 8
}

for naam in cijfers:
    cijfer = float(cijfers[naam]);

    if cijfer > 9:
        print(naam +  ": " + str(cijfer))