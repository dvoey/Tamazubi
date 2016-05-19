class OpBaum(object):
    def __init__(self):
        self.operator = ''
        self.nummer = 0.0
        self.linkerBaum = None
        self.rechterBaum = None

    def __init__(self, l):
        self.operator = ''
        self.nummer = 0.0
        self.linkerBaum = None
        self.rechterBaum = None

        re = []
        li = []
        op = ''

        if l[0] == '(' and l[-1] == ')':  # [0]=='(' and [::-1]==')':
            l = l[1:-1]

        # (3+5)*(2+4) bsp was nicht ginge
        #  Wenn Anzahl der Token in l gleich 1 ist, dann muss dieser Token eine Zahl sein
        if len(l) == 1:
            self.nummer = float(l[0])
            return

        while len(l) > 0:
            t = l[0]
            l = l[1:]

            if t.replace('.', '', 1).isdigit():  # Wenn t eine Zahl ist, haenge t an re
                re.append(t)

            elif t in ['+', '-']:  # Sonst Wenn t gleich + oder -
                if op != '':
                    li.append(op)
                li += re            # das gleiche wie li = li + re
                re = []
                op = t

            elif t in ['*', '/']:  #sonst Wenn t gleich * oder /
                if op == '+' or op == '-':
                    re.append(t)
                else:
                    if op != '':
                        li.append(op)

                    li += re
                    re = []
                    op = t


            elif t == '(': #Sonst Wenn t gleich (
                re.append(t)
                klammern = 1
                while klammern > 0:
                    s = l[0]
                    l = l[1:]

                    if s == ')':
                        klammern = klammern - 1

                    elif s == '(':
                        klammern = klammern + 1

                    re.append(s)

        if self.linkerBaum == None:
            self.linkerBaum = OpBaum(li)
            self.rechterBaum = OpBaum(re)
            self.operator = op




    def Berechnen(self):
        if self.operator == '':
            return self.nummer
        elif self.operator == '+':
            return self.linkerBaum.Berechnen() + self.rechterBaum.Berechnen()
        elif self.operator == '-':
            return self.linkerBaum.Berechnen() - self.rechterBaum.Berechnen()
        elif self.operator == '*':
            return self.linkerBaum.Berechnen() * self.rechterBaum.Berechnen()
        elif self.operator == '/':
            return self.linkerBaum.Berechnen() / self.rechterBaum.Berechnen()

    def GetFormel(self):
        if self.operator == '':
            return str(self.nummer)
        else:
            return '(' + self.linkerBaum.GetFormel() + self.operator + self.rechterBaum.GetFormel() + ')'


def Tokenize(formelstr):

    tokens = []
    zahl = ''

    while len(formelstr) > 0:
        z = formelstr[0]

        if z.isdigit() or z == '.':
            zahl = zahl + z


        elif z in ['(', '+', '-', ')', '*', '/']:
            if len(zahl) > 0:
                tokens.append(zahl)
                zahl = ''

            tokens.append(z)

        elif z == ' ':
            if len(zahl) > 0:
                tokens.append(zahl)
                zahl = ''



        formelstr = formelstr[1:]


    if len(zahl)>0:
        tokens.append(zahl)


    return tokens



tokens = Tokenize('(5+3)*4-7/2*8.5')
d = OpBaum(tokens)





print(d.GetFormel())
print(d.Berechnen())

