from datetime import datetime, timedelta


class Hungerverwaltung(object):

    def __init__(self):
        self.suesswert = 100 #0-100
        self.vitaminwert = 100 #0-100
        self.durstwert = 100 #0-100

    def laden(self, pfad): #nur spezifische werte geupdatet
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
                self.suesswert = float(split[1])
            if split[0] == 'VITAMINWERT':
                self.vitaminwert = float(split[1])
            if split[0] == 'DURSTWERT':
                self.durstwert = float(split[1])

        text.close()

        #Hungerwerte anhand der Uhrzeit aktualisieren
        punkte = int(deltatime.seconds / 3600)

        self.suesswert = self.suesswert - punkte*0.5
        self.vitaminwert = self.vitaminwert - punkte*1.5
        self.durstwert = self.durstwert - punkte*2

        if (self.suesswert < 0):
            self.suesswert = 0

        if (self.vitaminwert < 0):
            self.vitaminwert = 0

        if (self.durstwert < 0):
            self.durstwert = 0

    def speichern(self, text):
        text.write("SUESSWERT="+str(self.suesswert)+"\n")
        text.write("VITAMINWERT="+str(self.vitaminwert)+"\n")
        text.write("DURSTWERT="+str(self.durstwert)+"\n")


    def get_hungerwert(self): #gesamthungerwert
        return min(self.durstwert, self.vitaminwert, self.suesswert)

    def essen(self, deltaSuess, deltaVitamin, deltaDurst):
        self.suesswert = self.suesswert + deltaSuess
        self.vitaminwert += deltaVitamin
        self.durstwert += deltaDurst

        if self.suesswert > 100:
            self.suesswert = 100

        if self.vitaminwert > 100:
            self.vitaminwert = 100

        if self.durstwert > 100:
            self.durstwert = 100