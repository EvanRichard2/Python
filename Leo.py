from graphics import *

def main():
    win = GraphWin("straight", 400, 400)
    win.yUp()

    head = Circle(Point(100,200), 25)
    head.setWidth(4)
    head.draw(win)
   
	
	
    win.getMouse()
    win.Close()

main()

