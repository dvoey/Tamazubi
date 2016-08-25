# coding=utf-8
from datetime import datetime, timedelta
from random import *


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
                self.lernmotivation = float(split[1])
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

    def printStatus(self):
        print("Lernmotivation = " + str(self.lernmotivation) + ", Intelligenz = " + str(self.intelligenz))

    def lernen(self, deltaLernen):
        # deltaLernen wird von der Lernmotivation abgezogen (minimale Motivation ist 0)
        # Intelligenzzuwachs ist abhängig von der Lermotivation und dem deltaLernen
            # d.h. je größer die Lernmotivation desto größer der Intelligenzzuwachs
            #      je größer deltaLernen desto größer der Intelligenzzuwachs
        # Zufälliger Bonus beim Intelligenzzuwachs

        deltaLernenReal = deltaLernen if deltaLernen <= self.lernmotivation else self.lernmotivation

        if self.lernmotivation > 75:
            deltaIntelligenz = (0.5+uniform(0.0, 0.2)) * deltaLernenReal

        elif self.lernmotivation > 50:
            deltaIntelligenz = (0.3+uniform(0.0, 0.1)) * deltaLernenReal

        elif self.lernmotivation > 20:
            deltaIntelligenz = (0.2+uniform(0.0, 0.06)) * deltaLernenReal

        else:
            deltaIntelligenz = 0.05 * deltaLernenReal

        self.lernmotivation -= deltaLernenReal
        self.intelligenz += deltaIntelligenz

        return deltaIntelligenz
