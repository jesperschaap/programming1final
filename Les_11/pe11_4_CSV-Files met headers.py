import csv

def fmaken():
    bestand = 'index.csv'
    file = open(bestand, 'w', newline='')
    writer = csv.writer(file)

    writer.writerow(['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'])
    writer.writerow([121, 'ABC123', 'Highlight pen', 231, 0.56])
    writer.writerow([123, 'PQR678', 'Nietmachine', 587, 9.99])
    writer.writerow([128, 'ZYX163', 'Bureaulamp', 34, 19.95])
    writer.writerow([137, 'MLK709', 'Monitorstandaard', 66, 32.50])
    writer.writerow([271, 'TRS665', 'Ipad hoes', 155, 19.01])


def duurtsteartikel():
    bestand = 'index.csv'
    file = open(bestand, 'r')
    reader = csv.reader(file, delimiter =',')
    price = [" ", " ", " ", " ", 0];
    next(reader)
    for row in reader:
        if float(row[4]) > float(price[4]):
            price = row;
    highestprice = price[4]
    product = price[2]
    # print(highestprice, product)
    return product, highestprice

def loweststock():
    bestand = 'index.csv'
    file = open(bestand, 'r')
    reader = csv.reader(file, delimiter=',')
    stock = [" ", " ", " ", float('inf'), " "];
    next(reader)
    for row in reader:
        if float(row[3]) < float(stock[3]):
            stock = row;
    loweststock = stock[3]
    productid = stock[0]
    # print(loweststock, productid)
    return loweststock, productid

def stock():
    bestand = 'index.csv'
    file = open(bestand, 'r')
    reader = csv.reader(file, delimiter=',')
    stock = 0
    next(reader)
    for row in reader:
         stock += float(row[3])
    # print(int(stock))
    return int(stock)

def printall():
    pname, pprice = duurtsteartikel()
    plowstock, pid = loweststock()
    totalstock = stock()
    print("Het duurste artikel is ", pname, "en die kost ", pprice, " Euro")
    print("Er zijn slechts ", plowstock, " exemplaren in voorraad van het product met nummer ", pid)
    print("In totaal hebben wij ", totalstock, " producten in ons magazijn liggen")

# fmaken()
# duurtsteartikel()[:1]
# loweststock()
# stock()
printall()