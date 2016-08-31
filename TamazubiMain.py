from graphics import *
from Tamazubi import *


class TamazubiMain(object):

    def main():
        tamazubi = Tamazubi()

        win = GraphWin('Tamazubi', 500, 500) # give title and dimensions

        paintTamazubi(win)
        #
        win.mainloop()

        win.close()


    def paintTamazubi(window):
        head = Circle(Point(40,100), 52) # set center and radius
        head.setFill("yellow")
        head.draw(window)


main()


