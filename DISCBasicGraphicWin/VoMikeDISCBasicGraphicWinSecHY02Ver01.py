# Project:      DISC Basic Graphic Window (VoMikeDISCSecHY2Ver01.py)
# Name:         Mike Vo
# Date:         02/18/17
# Description:  This program creates Andy's 400 x 400 window using
#               the Graphics library.

from graphics import *

### drawAnysGraphics(GraphWinObj) ###
# Render Andy's set of shapes into GraphWinObj
def drawAndysGraphics(GraphWinObj):

    # Render the black rectangle and its labels
    topLabel = Text(Point(80 + (170 - 80)/2, 60), "Top")
    topLabel.setFill("green")
    topLabel.draw(GraphWinObj)
    bottomLabel = Text(Point(80 + (170 - 80)/2, 330), "Bottom")
    bottomLabel.setFill("green")
    bottomLabel.draw(GraphWinObj)
    blackRect = Rectangle(Point(80, 70), Point(170, 320))
    blackRect.setFill("black")
    blackRect.draw(GraphWinObj)

    # Render the three colors staircase
    purpleRect = Rectangle(Point(200, 200), Point(260, 230))
    purpleRect.setFill("purple")
    purpleRect.draw(GraphWinObj)
    orangeRect = Rectangle(Point(230, 170), Point(290, 200))
    orangeRect.setFill("orange")
    orangeRect.draw(GraphWinObj)
    blueRect = Rectangle(Point(260, 140), Point(320, 170))
    blueRect.setFill("blue")
    blueRect.draw(GraphWinObj)

    # Render the two cirles
    redCirc = Circle(Point(235, 300), 35)
    redCirc.setFill("red")
    redCirc.draw(GraphWinObj)
    yellowCirc = Circle(Point(270, 300), 35)
    yellowCirc.setFill("yellow")
    yellowCirc.draw(GraphWinObj)

def main():

    # Initialize a blank 400x400 window titled "Shapes"
    win = GraphWin("Shapes", 400, 400)

    # Render  Andy's graphics and wait for user input (in shell)
    drawAndysGraphics(win)
    input("Press Enter to close window")

    # Close window
    win.close()

main()
