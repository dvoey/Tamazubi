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
        haupt = Point(250,225)
        lArmWinkel = math.radians(135)


        head = Circle(Point(haupt.x, haupt.y-125), 52)  # set center and radius
        head.setFill("yellow")
        head.draw(window)

        koerper = Oval(Point(-50+haupt.x, -75+haupt.y), Point(50+haupt.x, 75+haupt.y))  # set center and radius
        koerper.setFill("black")
        koerper.draw(window)

        armEnde = Point(-150 * math.sin(lArmWinkel) + haupt.x-30, 150 * math.cos(lArmWinkel) +haupt.y-75)
        rArm = Line(Point(haupt.x-30, haupt.y-75),  armEnde)  # rArm
        rArm.setWidth(15)
        rArm.setFill("red")
        rArm.draw(window)

        # linker Arm


        lArm = Line(Point(haupt.x+30, haupt.y-75), Point(340, 250))  # lArm
        lArm.setWidth(15)
        lArm.setFill("blue")
        lArm.draw(window)

        rLeg = Line(Point(280, 285), Point(340, 450))  # rLeg
        rLeg.setWidth(15)
        rLeg.setFill("green")
        rLeg.draw(window)

        lLeg = Line(Point(220, 285), Point(140, 450))  # lLeg
        lLeg.setWidth(15)
        lLeg.setFill("purple")
        lLeg.draw(window)

        for i in range(20,135):
            ArmWinkel = math.radians(i)
            rArm.undraw()
            armEnde = Point(-150 * math.sin(lArmWinkel) + haupt.x - 30, 150 * math.cos(lArmWinkel) + haupt.y - 75)
            rArm.p2 = armEnde
            rArm.draw(window)
            time.sleep(0.05)

TamazubiMain.main()


