def standaardprijs(afstandKM):
    if afstandKM <= 50:
        return(str(afstandKM*0.80)+'euro')
    else:
        return(str(afstandKM*0.60+15)+'euro')
print(standaardprijs(51))

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit== 'true' and leeftijd <12 and leeftijd >=65:
        return(afstandKM*0,65)
    if weekendrit== 'true' and leeftijd >=12 and leeftijd <65:
        return

