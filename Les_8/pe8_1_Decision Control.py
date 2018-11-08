def seizoen(maand):
    if maand <= 0 or maand > 12:
        return('Er zit minimaal 1 maand in het jaar en maximaal 12 maanden')
    elif maand >= 3 and maand <= 5:
        return('lente')
    elif maand >=6 and maand <= 8:
        return('zomer')
    elif maand >= 9 and maand <= 11:
        return('herfst')
    else:
        return('winter')


for i in range(-2, 14, 1):
    print(seizoen(i))