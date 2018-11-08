aantal = 12;
file = open('kluizen.txt', 'r+')
lines = file.readlines()


def toon_aantal_kluizen_vrij():
    count = 0;

    for i in enumerate(lines):
        count += 1;

    print("Er zijn nog " + str(aantal - count) + " kluizen beschikbaar")
    file.close();


def nieuwe_kluis():
    kluizen = list(range(1, 13, 1));

    for line in lines:
        kluisnummer = int(line.split(";")[0]);
        # print(kluisnummer)
        kluizen.remove(kluisnummer);
    # print(kluizen)

    if len(kluizen) == 0 :
        print("Er zijn geen kluizen meer beschikbaar");
        return

    code = input('Code: ')
    kluisnummer = kluizen[0];
    file.write("\n" + str(kluisnummer) + ";" + code);
    print("Kluisnummer: " + str(kluisnummer));

def kluis_openen():
    kluisnummer = int(input("Kluisnummer: "));

    for line in lines:
        kluis = line.split(";");

        if kluisnummer == int(kluis[0]):
            kluiscode = input("Kluiscode: ");

            if kluiscode == kluis[1].rstrip("\n"):
                print("Kluis geopend!");
                return;
            else:
                print("Onjuiste gegevens");
                return;

            print("Kluis niet gevonden");

def kluis_inleveren():



print(
    "1: Ik wil weten hoeveel kluizen nog vrij zijn\n" +
    "2: Ik wil een nieuwe kluis\n" +
    "3: Ik wil even iets uit mijn kluis halen\n" +
    "4: Ik geef mijn kluis terug"
);

menukeuze = int(input("Menukeuze: "));

if menukeuze == 1:
    toon_aantal_kluizen_vrij();
elif menukeuze == 2:
    nieuwe_kluis();
elif menukeuze == 3:
    kluis_openen();
elif menukeuze == 4:
    kluis_inleveren();
else:
    print("Ongeldige menukeuze");



