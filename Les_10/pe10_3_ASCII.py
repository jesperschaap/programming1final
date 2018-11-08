def code(invoerstring):
    output = "";

    for char in invoerstring:
        output += chr(ord(char) + 3);

    return output

print(code("RutteAlkmaarDen Helder"));