cijferICOR=6
cijferPROG=8
cijferCSN=7
som = (cijferICOR+cijferCSN+cijferPROG)
gemiddelde = som / 3
beloning = som* 30
overzicht = 'mijn cijfers (gemiddeld een' + str(gemiddelde) + ') leveren een beloning ' + str(beloning)
print(overzicht)