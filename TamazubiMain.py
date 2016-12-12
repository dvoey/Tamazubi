from Tamazubi import *
import math
from Tkinter import *


class TamazubiMain(object):

    def __init__(self):
        # Fenster / Zeichenflaeche
        self.zeichenflaeche = None
        self.fenster = None

        # Tamazubi Aussehen / Konstanten
        self.laenge_koerper = 200
        self.laenge_arm = 180
        self.laenge_bein = 230
        self.radius_kopf = 40
        self.breite_koerper = 100
        self.breite_linkerarm = 30
        self.breite_rechterarm = 30
        self.breite_linkesbein = 40
        self.breite_rechtesbein = 40

        # Tamazubi IST
        self.ist_position_x = 500
        self.ist_position_y = 500
        self.ist_winkel_linkerarm = math.radians(0.0)
        self.ist_winkel_rechterarm = math.radians(-90.0)
        self.ist_winkel_linkesbein = math.radians(170.0)
        self.ist_winkel_rechtesbein = math.radians(190)

        # Tamazubi SOLL
        self.soll_position_x = 500
        self.soll_position_y = 500
        self.soll_winkel_linkerarm = math.radians(135.0)
        self.soll_winkel_rechterarm = math.radians(-135.0)
        self.soll_winkel_linkesbein = -10.0
        self.soll_winkel_rechtesbein = 10.0


    def init(self):
        self.fenster = Tk()

        self.zeichenflaeche = Canvas(self.fenster, width=1000, height=1000)
        self.zeichenflaeche.pack()
        self.animation()
        self.fenster.mainloop()

    def animation(self):
        self.zeichenflaeche.delete(ALL)

        # Neue Positionen
        delta = (self.soll_winkel_linkerarm - self.ist_winkel_linkerarm)
        if delta < -0.1:
            self.ist_winkel_linkerarm = self.ist_winkel_linkerarm - 0.1
        elif delta > 0.1:
            self.ist_winkel_linkerarm = self.ist_winkel_linkerarm + 0.1
        else:
            self.ist_winkel_linkerarm = self.soll_winkel_linkerarm

        delta = (self.soll_winkel_rechterarm - self.ist_winkel_rechterarm)
        if delta < -0.1:
            self.ist_winkel_rechterarm = self.ist_winkel_rechterarm - 0.1
        elif delta > 0.1:
            self.ist_winkel_rechterarm = self.ist_winkel_rechterarm + 0.1
        else:
            self.ist_winkel_rechterarm = self.soll_winkel_rechterarm


        #Positionen
        #haupt = CENTER(500, 500)
        #ist_winkel_linkerarm = soll_winkel_linkerarm

        # Koerper
        self.zeichenflaeche.create_line(self.ist_position_x,
                                        self.ist_position_y-0.5*self.laenge_koerper,
                                        self.ist_position_x,
                                        self.ist_position_y+0.5*self.laenge_koerper,
                                        width=self.breite_koerper)
        # #Kopf
        self.zeichenflaeche.create_oval(self.ist_position_x-0.75*self.radius_kopf,
                                        self.ist_position_y-1*self.laenge_koerper,
                                        self.ist_position_x+0.75*self.radius_kopf,
                                        self.ist_position_y-0.5*self.laenge_koerper,
                                        fill="black"
                                        )

        # Rechter Arm
        arm_x = -self.laenge_arm * math.sin(self.ist_winkel_rechterarm) + self.ist_position_x+0.5*self.breite_koerper
        arm_y = -self.laenge_arm * math.cos(self.ist_winkel_rechterarm) + self.ist_position_y-0.5*self.laenge_koerper

        self.zeichenflaeche.create_line(self.ist_position_x+0.5*self.breite_koerper,
                                        self.ist_position_y-0.5*self.laenge_koerper, arm_x, arm_y,
                                        width=self.breite_rechterarm)

        # Linker Arm
        arm_x = -self.laenge_arm * math.sin(self.ist_winkel_linkerarm) + self.ist_position_x - 0.5 * self.breite_koerper
        arm_y = -self.laenge_arm * math.cos(self.ist_winkel_linkerarm) + self.ist_position_y - 0.5 * self.laenge_koerper

        self.zeichenflaeche.create_line(self.ist_position_x - 0.5 * self.breite_koerper,
                                        self.ist_position_y - 0.5 * self.laenge_koerper, arm_x, arm_y,
                                        width=self.breite_linkerarm)

        # Rechtes Bein
        bein_x = -self.laenge_bein * math.sin(self.ist_winkel_rechtesbein) + self.ist_position_x + 0.5 * self.breite_koerper
        bein_y = -self.laenge_bein * math.cos(self.ist_winkel_rechtesbein) + self.ist_position_y + 0.5 * self.laenge_koerper

        self.zeichenflaeche.create_line(self.ist_position_x + 0.5 * self.breite_koerper,
                                        self.ist_position_y + 0.5 * self.laenge_koerper, bein_x, bein_y,
                                        width=self.breite_rechtesbein)

        # Linkes Bein
        bein_x = -self.laenge_bein * math.sin(self.ist_winkel_linkesbein) + self.ist_position_x - 0.5 * self.breite_koerper
        bein_y = -self.laenge_bein * math.cos(self.ist_winkel_linkesbein) + self.ist_position_y + 0.5 * self.laenge_koerper

        self.zeichenflaeche.create_line(self.ist_position_x - 0.5 * self.breite_koerper,
                                        self.ist_position_y + 0.5 * self.laenge_koerper, bein_x, bein_y,
                                        width=self.breite_linkesbein)

        #Animation ausfuehren
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
