def Tokenize(formelstr):

    tokens = []
    zahl = ''

    while len(formelstr)>0:
        z = formelstr[0]

        if z.isdigit() or z == '.':
            zahl = zahl + z


        elif z in ['(', '+', '-', ')', '*', '/']:
            if len(zahl)>0:
                tokens.append(zahl)
                zahl = ''

            tokens.append(z)

        elif z == ' ':
            if len(zahl)>0:
                tokens.append(zahl)
                zahl = ''



        formelstr = formelstr[1:]


    if len(zahl)>0:
        tokens.append(zahl)


    return tokens


toks = Tokenize("5-2-1")
print(toks)
