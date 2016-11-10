from Tamazubi import *
import math
from Tkinter import *


class TamazubiMain(object):

    def __init__(self):
        self.zeichenflaeche = None
        self.fenster = None

        self.ist_winkel_linkerarm = 2.0
        self.soll_winkel_linkerarm = 50.0

    def init(self):
        self.fenster = Tk()

        self.zeichenflaeche = Canvas(self.fenster, width=1000, height=1000)
        self.zeichenflaeche.pack()
        self.animation()
        self.fenster.mainloop()

    def animation(self):
        self.zeichenflaeche.delete(ALL)

        self.fenster.after(20, self.animation)
    #def paintTamazubi(window):

        # # Positionen
        # haupt = Point(250, 225)
        # rArmWinkel = math.radians(135)
        # rLegWinkel = math.radians(20)
        # lArmWinkel = math.radians(135)
        # lLegWinkel = math.radians(20)
        # #Kopf
        # head = Circle(Point(haupt.x, haupt.y-125), 52)  # set center and radius
        # head.setFill("yellow")
        # head.draw(window)
        # #Koerper
        # koerper = Oval(Point(-50+haupt.x, -75+haupt.y), Point(50+haupt.x, 75+haupt.y))  # set center and radius
        # koerper.setFill("black")
        # koerper.draw(window)
        # #Rechter Arm
        # rarmEnde = Point(-150 * math.sin(rArmWinkel) + haupt.x-30, 150 * math.cos(rArmWinkel) +haupt.y-75)
        # rArm = Line(Point(haupt.x-30, haupt.y-75), rarmEnde)  # rArm
        # rArm.setWidth(15)
        # rArm.setFill("red")
        # rArm.draw(window)
        # #linker Arm
        # larmEnde = Point(150 * math.sin(lArmWinkel) + haupt.x + 30, -150 * math.cos(lArmWinkel) + haupt.y - 75)
        # lArm = Line(Point(haupt.x+30, haupt.y-75), larmEnde)  # lArm
        # lArm.setWidth(15)
        # lArm.setFill("blue")
        # lArm.draw(window)
        # #linkes Bein
        # lLegEnde = Point(200 * math.sin(lLegWinkel) + haupt.x + 30, 200 * math.cos(lLegWinkel) + haupt.y + 75)
        # lLeg = Line(Point(haupt.x+30, haupt.y+60), lLegEnde)
        # lLeg.setWidth(15)
        # lLeg.setFill("green")
        # lLeg.draw(window)
        # #Rechtes Bein
        # rLegEnde = Point(-200 * math.sin(rLegWinkel) + haupt.x - 30, 200 * math.cos(rLegWinkel) + haupt.y + 75)
        # rLeg = Line(Point(haupt.x-30, haupt.y+60), rLegEnde)  # rechterLeg
        # rLeg.setWidth(15)
        # rLeg.setFill("purple")
        # rLeg.draw(window)
        #
        # # Rechter Arm und rechtes Bein
        # for i in range(20, 135):
        #     rArmWinkel = math.radians(i)
        #     rArm.undraw()
        #     rarmEnde = Point(-150 * math.sin(rArmWinkel) + haupt.x - 30, 150 * math.cos(rArmWinkel) + haupt.y - 75)
        #     rArm.p2 = rarmEnde
        #     rArm.draw(window)
        #     rLegWinkel = math.radians(i)
        #     rLeg.undraw()
        #     rLegEnde = Point(-200 * math.sin(rLegWinkel) + haupt.x - 30, 200 * math.cos(rLegWinkel) + haupt.y + 75)
        #     rLeg.p2 = rLegEnde
        #     rLeg.draw(window)
        #     time.sleep(0.008)
        #
        # # Linker Arm und linkes Bein
        # for i in range(50, 135):
        #     lArmWinkel = math.radians(i)
        #     lArm.undraw()
        #     larmEnde = Point(150 * math.sin(lArmWinkel) + haupt.x + 30, 150 * math.cos(lArmWinkel) + haupt.y - 75)
        #     lArm.p2 = larmEnde
        #     lArm.draw(window)
        #     lLegWinkel = math.radians(i)
        #     lLeg.undraw()
        #     lLegEnde = Point(200 * math.sin(lLegWinkel) + haupt.x + 30, 200 * math.cos(lLegWinkel) + haupt.y + 75)
        #     lLeg.p2 = lLegEnde
        #     lLeg.draw(window)
        #     time.sleep(0.008)

fenster = TamazubiMain()

fenster.init()
