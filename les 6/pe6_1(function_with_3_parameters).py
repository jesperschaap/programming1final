def som(getal_1,getal_2,getal_3):
    opsomming = getal_1+getal_2+getal_3
    print('getal_2 is '+str(getal_2))
    print('getal_3 is '+str(getal_3))
    print(opsomming)
    antwoord= int(input('hoeveel is getal_1?'))
    if antwoord ==getal_1:
        return("good job")
    else:
        return('try again')

print(som(1,5,10))
