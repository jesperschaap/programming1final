def convert(tc):
    tf = tc * 1.8 + 32;
    return tf

def table(min,max):
    print('{0:<}{1:>10}'.format("Fahrenheit", "Celcius"))
    for i in range(min,max+1,10):
        fr = f=str(i)
        ce = c=str(convert(i))
        print('{f:>3}{c:>15}'.format(f=fr,c=ce))
    return '--------------------'

print(table(-30,40));



