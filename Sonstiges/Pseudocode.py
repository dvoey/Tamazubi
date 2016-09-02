class Baum:

    def liste(self, op, li=None, re=None):
        self.op = op
        self.li = li
        self.re = re
        l = []
        zahl = ''

        while len(liste) > 0:
            t = l[0]

            if l[0] == '(' and l[-1] == ')':  # [0]=='(' and [::-1]==')':
                del l[0]
                del l[:-1]  # l.remove('(') and l.remove(')')

            elif l.isdigit() or l == '.':  # Wenn t eine Zahl ist, haenge t an re
                l = []
                t.append(re)
                zahl = zahl + t


            elif t in ['+', '-']:  # Sonst Wenn t gleich + oder -
                t.append(li)
                re.append(li)
                l.remove(re)
                zahl = ''
                op = t

            elif t in ['*', '/']:  #sonst Wenn t gleich * oder /
                if op != '':
                    op.append(re)

                re.append(li)
                l.remove(re)
                op = t

            elif t == ['(']:  #Sonst Wenn t gleich (
                t.append(re)
                klammern = 1
                while klammern == 0:
                    s = l[0]

                    if s == '(':
                        klammern - 1

                    elif s == ')':
                        klammern + 1

                    s.append(re)


b = Baum()
ausgabe = b.liste('5+2*3')
print(ausgabe)