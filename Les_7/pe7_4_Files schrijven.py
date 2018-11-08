import datetime


def hardlopers():
    i = 1
    fw = open('hardlopers.txt', 'w')
    while i <6:
        i += 1
        naam = input('Welke hardloper is er zojuist binnen gekomen? ')
        nu = datetime.datetime.today();

        fw.write(nu.strftime("%a %d %b %Y, %X") + ", " + naam + "\n");

    fw.close()

hardlopers()


# import datetime;
#
# file = open("hardlopers.txt", "a");
#
# nu = datetime.datetime.today();
# naam = input("Naam: ");
#
# file.write(nu.strftime("%a %d %b %Y, %X") + ", " + naam + "\n");