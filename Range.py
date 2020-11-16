def get_alphabets(startletter, stopletter, step):
    for c in range(ord(startletter.lower()), ord(stopletter.lower()), step):
        yield chr(c)

print(list(get_alphabets("a", "h", 1)))