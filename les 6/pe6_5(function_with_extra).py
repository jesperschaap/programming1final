def kwadraten_som(grondgetallen):
    return sum([i**2 for i in grondgetallen if i>0])

print(kwadraten_som([6,5,4,3,-2]))