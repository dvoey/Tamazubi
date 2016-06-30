# coding=utf-8

class Tamazubi(object):

    def __init__(self,pfad):
        self.name = ""
        self.alter = -1
        self.ausbildungstyp = ""

        self.laden(pfad)

        if self.name == "":
            self.name = raw_input('Wie heißt du?')

        if self.alter == -1:
            self.alter = int(raw_input('Wie alt bist du?'))

        if self.ausbildungstyp == "":
            self.ausbildungstyp = raw_input('Was ist deine Ausbildung?')


    def speichern(self):
        text = open('c:/temp/test.txt', 'w')
        text.write("NAME="+self.name+"\n")
        text.write("ALTER="+str(self.alter)+"\n")
        text.write("AUSBILDUNG="+self.ausbildungstyp+"\n")
        text.close()

    def laden(self,pfad):
        text = open(pfad, 'r')

        while True:
            zeile = text.readline()
            if zeile == '':
                break

            split = zeile.split("=", 1)

            if split[0] == 'NAME':
                self.name = split[1]

            if split[0] == 'ALTER':
                self.alter = int(split[1])

            if split[0] == 'AUSBILDUNG':
                self.ausbildungstyp = split[1]

        text.close()

t = Tamazubi('c:/temp/test.txt') #azubiname,azubialter,azubityp)
t.speichern()
#t.laden()