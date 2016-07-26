from datetime import datetime, timedelta


class Hungerverwaltung(object):

    def __init__(self):
        self.suesswert = -1 #0-100
        self.vitaminwert = -1 #0-100
        self.durstwert = -1 #0-100

    def update(self, timedelta): #nur spezifische werte geupdatet
        text = open('c:/temp/test.txt', 'r')

        while True:
            zeile = text.readline()
            if zeile == '':
                break

            split = zeile.replace("\n", "").split("=", 1)

            if split[0] == 'HUNGER':
                self.hminWert = int(split[1])

    def get_hungerwert(self): #gesamthungerwert
        hungerwertliste = [self.suesswert, self.vitaminwert, self.durstwert]
        hminWert = min(hungerwertliste)
        print(hminWert)

hminWert = -1 #0-100

DeltaZeit = alte Zeit - neue Zeit #in minuten konvertieren

    if suesswert > 0:
        then Ergebnis = hWert - round(DeltaZeit/2.5)
        if (Ergebnis < 0): ergebnis =0
        print(Ergebnis)

    if vitaminwert > 0:
        then Ergebnis = hWert - round(DeltaZeit/3.5)
        if (Ergebnis < 0): ergebnis =0
        print(Ergebnis)

    if durstwert > 0:
        then Ergebnis = hWert - round(DeltaZeit/2)
        if (Ergebnis < 0): ergebnis =0
        print(Ergebnis)

    if suesswert or vitaminwert or durstwert <= 35:
        print ("Bitte füttern!")

    Ergebnis = hWert

    def speichern(self):
        text = open('c:/temp/test.txt', 'w')
        text.write("ZEIT="+str(datetime.now())+"\n")
        text.write("NAME="+self.name+"\n")
        text.write("ALTER="+str(self.alter)+"\n")
        text.write("AUSBILDUNG="+self.ausbildungstyp+"\n")
        text.write("HUNGER="+str(self.hWert)+"\n")

        text.close()

