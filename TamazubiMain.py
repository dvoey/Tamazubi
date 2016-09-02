from Tamazubi import *
from graphics import *


class TamazubiMain(object):

    @staticmethod
    def main():
        #tamazubi = Tamazubi()

        win = GraphWin('Tamazubi', 500, 500) # give title and dimensions

        t.paintTamazubi(win)

        win.mainloop()

        win.close()


    def paintTamazubi(window):
        head = Circle(Point(40,100), 52) # set center and radius        #head
        head.setFill("yellow")
        head.draw(window)

        rArm = Line(Point(40, 100), 52)   #rArm
        rArm.setFill("red")
        rArm.draw(window)

        lArm = Line(Point(40, 100), 52)     #lArm
        lArm.setFill("blue")
        lArm.draw(window)

        rLeg = Line(Point(40, 100), 52)       #rLeg
        rLeg.setFill("green")
        rLeg.draw(window)

        lLeg = Line(Point(40, 100), 52)       #lLeg
        lLeg.setFill("purple")
        lLeg.draw(window)

TamazubiMain.main()


