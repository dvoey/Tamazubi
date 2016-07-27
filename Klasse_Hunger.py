from datetime import datetime, timedelta


class Hungerverwaltung(object):

    def __init__(self):
        self.suesswert = 100 #0-100
        self.vitaminwert = 100 #0-100
        self.durstwert = 100 #0-100

    def laden(self,pfad): #nur spezifische werte geupdatet
        deltatime = timedelta(0, 0, 0, 0)
        text = open(pfad, 'r')

        while True:
            zeile = text.readline()
            if zeile == '':
                break

            split = zeile.replace("\n", "").split("=", 1)

            if split[0] == 'ZEIT':
                deltatime = datetime.now() - datetime.strptime(split[1], "%Y-%m-%d %H:%M:%S.%f")
            if split[0] == 'SUESSWERT':
                self.suesswert = int(split[1])
            if split[0] == 'VITAMINWERT':
                self.vitaminwert = int(split[1])
            if split[0] == 'DURSTWERT':
                self.durstwert = int(split[1])

        text.close()

        # Hungerwerte anhand der Uhrzeit aktualisieren
        punkte = int(deltatime.seconds / 60)

        self.suesswert = self.suesswert - punkte
        self.vitaminwert = self.vitaminwert - punkte
        self.durstwert = self.durstwert - punkte


    def speichern(self, text):
        text.write("SUESSWERT="+str(self.suesswert)+"\n")
        text.write("VITAMINWERT="+str(self.vitaminwert)+"\n")
        text.write("DURSTWERT="+str(self.durstwert)+"\n")


    def get_hungerwert(self): #gesamthungerwert
       return min(self.durstwert, self.vitaminwert, self.suesswert)

# hminWert = -1 #0-100
# alteZeit = datetime.strptime(split[1])
# neueZeit = datetime.now()
#
# DeltaZeit = alteZeit - neueZeit #in minuten konvertieren
#
# if suesswert > 0:
#     Ergebnis = hWert - round(DeltaZeit/2.5)
#     if (Ergebnis < 0): ergebnis =0
#     print(Ergebnis)
#
# if vitaminwert > 0:
#     Ergebnis = hWert - round(DeltaZeit/3.5)
#     if (Ergebnis < 0): ergebnis =0
#     print(Ergebnis)
#
# if durstwert > 0:
#     Ergebnis = hWert - round(DeltaZeit/2)
#     if (Ergebnis < 0): ergebnis =0
#     print(Ergebnis)
#
# if suesswert or vitaminwert or durstwert <= 35:
#     print ("Bitte fuettern!")
#
#     Ergebnis = hWert



