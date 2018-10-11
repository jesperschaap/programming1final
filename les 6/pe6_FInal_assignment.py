# def standaardprijs(afstandKM):
#     if afstandKM <= 50:
#         return(str(afstandKM*0.80)+'euro')
#     else:
#         return(str(afstandKM*0.60+15)+'euro')
# print(standaardprijs(51))

def standaardprijs(afstandKM):
    if afstandKM <= 50:
        return(afstandKM*0.80)
    else:
        return(afstandKM*0.60+15)
print(standaardprijs(51))


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardtarief= standaardprijs(afstandKM)
    if weekendrit== True and( leeftijd <12 or leeftijd >=65):
        return(standaardtarief*0.65)
    if weekendrit== True and( leeftijd >=12 or leeftijd <65):
        return(standaardtarief*0.60)
    if weekendrit== False and( leeftijd <12 or leeftijd >=65):
        return(standaardtarief*0.70)
    if weekendrit== False and( leeftijd >=12 or leeftijd <65):
        return(standaardtarief*1)

print(ritprijs(11,False,51))
