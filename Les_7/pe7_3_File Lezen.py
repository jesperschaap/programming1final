# def bestand(file):
#     file = open(file,'r');
#     count = 0
#     lines = file.readlines()
#     for i,line in enumerate(file):
#         count += 1;
#     print(count);


def uitvoer(file):
    file = open(file, 'r')
    lines = file.readlines()
    count = 0
    biggest_number = 0
    biggest_line = 0
    for i,line in enumerate(lines):
        number = int(line.split(', ')[0])
        count += 1
        if number > biggest_number:
            biggest_number = number
            biggest_line = i


    print('Deze file telt ' + str(count) + ' regels')
    print('Het grootste kaartnummer is: '+ str(biggest_number) + ' en dat staat op regel ' + str(biggest_line+1))

uitvoer('kaartnummers.txt')
