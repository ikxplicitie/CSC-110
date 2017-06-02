# Project:      Lab09 (VoMikeLab09SecHY02Ver01.py)
# Name:         Mike Vo
# Date:         03/06/17
# Description:  This program will display a graph of score from a text file onto a graphic window

from graphics import *

# Read the input file
def ReadScores(strFileName):

    lstScores = []

    inFile = open(strFileName, "r")
    for strLine in inFile:
        lstScores.append(int(strLine))

    return lstScores

# Display the scale
def SetScale(pOrigin, GraphWinObj):

    for intScale in range(0, 101, 10):
        lblScale = Text(Point(pOrigin.getX() + intScale * 4.5, pOrigin.getY()), str(intScale))
        lblScale.setTextColor("gray")
        lblScale.draw(GraphWinObj)

# Render the graph
def RenderGraph(strTitle, lstData, GraphWinObj):

    # Initialize colors
    lstColors = ["red", "purple", "green", "brown", "orange"]

    # Render graph title
    lblTitle = Text(Point(GraphWinObj.getWidth() / 2, 25), strTitle)
    lblTitle.setSize(20)
    lblTitle.setStyle("bold")
    lblTitle.draw(GraphWinObj)

    SetScale(Point(20, GraphWinObj.getHeight() - 25), GraphWinObj)
    for intIndex in range(len(lstData)):

        # Draw the bar
        bar = Rectangle(Point(20, (50 + intIndex * 50) + 10), Point(20 + lstData[intIndex] * 4.5, (50 + intIndex * 50) + 45))
        bar.setOutline(lstColors[intIndex % len(lstColors)])
        bar.setFill(lstColors[intIndex % len(lstColors)])
        bar.draw(GraphWinObj)

        # Draw the data label
        intDataLabelX = bar.getP2().getX()
        if intDataLabelX < 70:
            intDataLabelX += 15
            strDataLabelColor = "black"
        else:
            intDataLabelX -= 15
            strDataLabelColor = "white"

        dataLabel = Text(Point(intDataLabelX, bar.getCenter().getY()), str(lstData[intIndex]))
        dataLabel.setTextColor(strDataLabelColor)
        dataLabel.draw(GraphWinObj)


def main():

    # Initialize
    win = GraphWin("Test Scores", 500, 350)
    win.setBackground("khaki")

    # Read file & Render
    lstScores = ReadScores("scores.txt")
    RenderGraph("5 Test Scores", lstScores, win)

    # Wait for user click then close
    win.getMouse()
    win.close()

main()