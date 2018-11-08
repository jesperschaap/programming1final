try:
    amount = int(input('Hoeveel mensen gaan er mee op reis? '))

    if amount == 0:
        print('Delen door nul kan niet!')
    elif amount <= 0:
        print('Negatieve getallen kunnen niet')
    else:
        print('De reis kost', str(4356 / amount), 'per persoon')

except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')