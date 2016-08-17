# coding=utf-8
from datetime import datetime, timedelta
from random import random


class Lernmotivationverwaltung(object):

    def __init__(self):
        self.lernmotivation = 100 #0-100
        self.intelligenz = 100 #0-200

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
            if split[0] == 'LERNMOTIVATION':
                self.lernmotivation = int(split[1])
            if split[0] == 'INTELLIGENZ':
                self.intelligenz = int(split[1])

        text.close()

        # lernmotivation anhand der Uhrzeit aktualisieren
        punkte = int(deltatime.seconds / 3600)

        self.lernmotivation = self.lernmotivation + punkte*0.3

        if (self.lernmotivation > 100):
            self.lernmotivation = 100

    def speichern(self, text):
        text.write("LERNMOTIVATION="+str(self.lernmotivation)+"\n")
        text.write("INTELLIGENZ="+str(self.intelligenz)+"\n")

    def lernen(self, deltaLernen, deltaIntelligenz):
        self.lernmotivation += deltaLernen
        self.intelligenz += deltaIntelligenz

        if self.lernmotivation < 0:
            self.lernmotivation = 0
            print ("Ich will nicht lernen.")
        if self.lernmotivation < 20:
            print ("Ich will nicht lernen.")
        if self.lernmotivation < 50:
            print ("Ich will noch etwas ausruhen.")
        if self.lernmotivation > 50:
            self.lernmotivation -= deltaLernen
            self.intelligenz = self.intelligenz + random.randint(1,6)