lijst = eval(input("Geef lijst met minimaal 10 strings: "))

def vierletter(lijst):
    vls = []
    for x in lijst:
        if len(x) == 4:
            vls.append(x)
    print('De nieuw-gemaakte lijst met alle vier-letter strings is: ')
    return vls

print(vierletter(lijst))