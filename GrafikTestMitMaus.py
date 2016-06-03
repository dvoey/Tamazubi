from graphics import *
import random


def main():
    win = GraphWin('FaceTest', 500, 500) # give title and dimensions

    entry = Entry(Point(300,150),50)
    entry.setFill("white")
    entry.draw(win)

    text = entry.getText()

    head = Circle(Point(40,100), 52) # set center and radius
    head.setFill("yellow")
    head.draw(win)
    #
    win.mainloop()
    # for i in range(10):
    #     eye1 = Circle(Point(random.randint(0,500), random.randint(0,500)), 5)
    #     col = "#" + str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
    #     eye1.setFill(col)
    #     eye1.draw(win)
    #
    # for i in range(10):
    #     #eye1 = Circle(Point(random.randint(0,500), random.randint(0,500)), 5)
    #     #col = "#" + str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
    #     #eye1.setFill(col)
    #     head.move(20, 60)
    #     head.draw(win)

#    if win.getMouse():
#
#        punkt = Circle(Point(getMouse.position), 2)
#        punkt.setFill("Black")
#        print m.click

    # punktListe = []
    # p = win.getMouse()
    # punktListe.append(p)
    #
    # for i in range(10):
    #     p2 = win.getMouse()
    #     for p1 in punktListe:
    #         kreis = Line(p1, p2)
    #        # kreis.setWidth(random.randint(2,15))
    #         kreis.setWidth(2)
    #         kreis.setFill("#" + str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99)))
    #         kreis.draw(win)
    #
    #     punktListe.append(p2)

  #  win.getMouse()
    win.close()

main()