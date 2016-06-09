# coding=utf-8

class Tamazubi(object):

    def __init__(self,name,alter,ausbildungstyp):
        self.name = name
        self.alter = alter
        self.ausbildungstyp = ausbildungstyp

    def speichern(self):
        text = open('c:/temp/test.txt', 'w')
        text.write("NAME="+self.name+"\n")
        text.write("ALTER="+self.alter+"\n")
        text.write("AUSBILDUNG="+self.ausbildungstyp+"\n")
        text.close()

    def laden(self):
        text = open('c:/temp/test.txt', 'r')

        # do
        #    zeile = readline()
        #    if zeile == ""
        #        break;
        #    split...
        #    if NAME
        #       ...
        #    ..


        for i in range(3):
            zeile = text.readline()
            split = zeile.split("=", 1)

            if split[0] == 'NAME':
                self.name = split[1]

            if split[0] == 'ALTER':
                self.alter = split[1]

            if split[0] == 'AUSBILDUNG':
                self.ausbildungstyp = split[1]

azubiname = raw_input('Wie heißt du?')
azubialter = raw_input('Wie alt bist du?')
azubityp = raw_input('Was ist deine Ausbildung?')

t = Tamazubi(azubiname,azubialter,azubityp)
t.speichern()
t.laden()