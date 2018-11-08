def ticker(filename):
    file = open(filename, 'r')
    lines = file.readlines();
    symbols = {};
    for line in lines:
        line = line.rstrip("\n");
        values = line.split(":");

        symbols[values[0]] = values[1];

    return symbols;

def companysearch():
    symbols = ticker("symbols.txt");
    name = input('Enter company name: ')
    return(symbols[name])


print(companysearch())
