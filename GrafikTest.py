from graphics import *

def main():
    win = GraphWin('FaceTest', 500, 150) # give title and dimensions


    head = Circle(Point(40,100), 52) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    #win.getMouse()
    eye2 = Circle(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setFill('blue')
    eye2.setWidth(10)
    eye2.draw(win)

    win.getMouse()
    mouth = Oval(Point(30, 120), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    win.getMouse()
    label = Text(Point(100, 120), 'A face')
    label.setFill('red')
    label.draw(win)
#
    win.getMouse()
    win.close()

main()