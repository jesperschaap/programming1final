import csv

def highestscore():
    bestand = 'gamers.csv'
    file = open(bestand)
    reader = csv.reader(file, delimiter = ';')
    score = [" ", " ", 0];
    for row in reader:
        if int(row[2]) > int(score[2]):
            score = row;
    print(score)

highestscore()