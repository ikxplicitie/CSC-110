# Project:      Lab08 (VoMikeLab08SecHY02Ver01.py)
# Name:         Mike Vo
# Date:         02/27/2017
# Description:  This program will create a graphics window program
#               that will display the 5th side of a dice

from graphics import *

# Draw a black dot at specified coordinate on specified window object
def Dot(centerPointX, centerPointY, GraphWinObj):

    dot = Circle(Point(centerPointX, centerPointY), 30)
    dot.setFill("black")
    dot.setOutline("black")
    dot.draw(GraphWinObj)

# Draw the 5th side of the dice (evoke Dot() for the dots)
def Dice(GraphWinObj):

    # Draw the white body
    diceBody = Rectangle(Point(100, 50), Point(400, 350))
    diceBody.setFill("white")
    diceBody.setOutline("white")
    diceBody.draw(GraphWinObj)

    # Draw the 5 dots
    Dot(diceBody.getCenter().getX(), diceBody.getCenter().getY(), GraphWinObj)
    Dot(diceBody.getCenter().getX() - 75, diceBody.getCenter().getY() - 75, GraphWinObj)
    Dot(diceBody.getCenter().getX() + 75, diceBody.getCenter().getY() - 75, GraphWinObj)
    Dot(diceBody.getCenter().getX() - 75, diceBody.getCenter().getY() + 75, GraphWinObj)
    Dot(diceBody.getCenter().getX() + 75, diceBody.getCenter().getY() + 75, GraphWinObj)

def main():

    # Initialize a blank khaki 500x400 window
    win = GraphWin("Lab08 - Mike Vo", 500, 400)
    win.setBackground("khaki")

    # Draw the dice
    Dice(win)

    # Pause for user click
    win.getMouse()

    # Close window
    win.close()

main()