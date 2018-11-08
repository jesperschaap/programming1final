woord = ' ';
while len(woord) != 0:
    woord = input('Geef een string van vier letters: ')

    if len(woord) == 4:
        break;

    print(woord, ' heeft ', len(woord), ' letters')

print('Inlezen van correcte string: ', woord, ' is geslaagd')

