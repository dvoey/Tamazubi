from Tamazubi import *
from graphics import *
import math


class TamazubiMain(object):

    @staticmethod
    def main():
        #tamazubi = Tamazubi()

        win = GraphWin('Tamazubi', 500, 500) # give title and dimensions

        TamazubiMain.paintTamazubi(win)

        win.mainloop()

        win.close()

    @staticmethod
    def paintTamazubi(window):

        # Positionen
        haupt = Point(250, 225)
        rArmWinkel = math.radians(135)
        rLegWinkel = math.radians(20)


        head = Circle(Point(haupt.x, haupt.y-125), 52)  # set center and radius
        head.setFill("yellow")
        head.draw(window)

        koerper = Oval(Point(-50+haupt.x, -75+haupt.y), Point(50+haupt.x, 75+haupt.y))  # set center and radius
        koerper.setFill("black")
        koerper.draw(window)

        armEnde = Point(-150 * math.sin(rArmWinkel) + haupt.x-30, 150 * math.cos(rArmWinkel) +haupt.y-75)
        rArm = Line(Point(haupt.x-30, haupt.y-75),  armEnde)  # rArm
        rArm.setWidth(15)
        rArm.setFill("red")
        rArm.draw(window)

        # linker Arm
        lArm = Line(Point(haupt.x+30, haupt.y-75), Point(340, 250))  # lArm
        lArm.setWidth(15)
        lArm.setFill("blue")
        lArm.draw(window)

        #rLeg = Line(Point(280, 285), Point(340, 450))  # rLeg
        lLeg = Line(Point(haupt.x+30, haupt.y+60), Point(340, 450))  # linkerLeg
        lLeg.setWidth(15)
        lLeg.setFill("green")
        lLeg.draw(window)

        rLegEnde = Point(-200 * math.sin(rLegWinkel) + haupt.x - 30, 200 * math.cos(rLegWinkel) + haupt.y + 75)
        rLeg = Line(Point(haupt.x-30, haupt.y+60), rLegEnde)  # rechterLeg
        #rLeg = Line(Point(haupt.x-30, haupt.y+60), Point(140, 450))  # rechterLeg
        rLeg.setWidth(15)
        rLeg.setFill("purple")
        rLeg.draw(window)

        for i in range(20, 135):
            rArmWinkel = math.radians(i)
            rArm.undraw()
            armEnde = Point(-150 * math.sin(rArmWinkel) + haupt.x - 30, 150 * math.cos(rArmWinkel) + haupt.y - 75)
            rArm.p2 = armEnde
            rArm.draw(window)
            time.sleep(0.05)

        # for i in range(-20, 80):
        #     rArmWinkel = math.radians(i)
        #     rArm.undraw()
        #     armStart = Point(-150 * math.sin(rArmWinkel) + haupt.x - 30, 150 * math.cos(rArmWinkel) + haupt.y - 75)
        #     armEnde = armStart
        #     rArm.draw(window)
        #     time.sleep(0.05)

        for i in range(20, 335): #RechtesBein
            rLegWinkel = math.radians(i)
            rLeg.undraw()
            rLegEnde = Point(-200 * math.sin(rLegWinkel) + haupt.x - 30, 200 * math.cos(rLegWinkel) + haupt.y + 75)
            rLeg.p2 = rLegEnde
            rLeg.draw(window)
            time.sleep(0.05)

TamazubiMain.main()


