from graphics import *

def GetRectangle(GraphWinObj):

    lstRectangleData = [
        # Area
        0.0,
        # Perimeter
        0.0
    ]

    p1 = GraphWinObj.getMouse()
    p1.draw(GraphWinObj)

    p2 = GraphWinObj.getMouse()
    p2.draw(GraphWinObj)

    rect = Rectangle(p1, p2)
    rect.setFill("pink")
    rect.setOutline("purple")
    rect.draw(GraphWinObj)

    p1.undraw()
    p2.undraw()

    fltLength = abs(p2.getX() - p1.getX())
    fltWidth = abs(p2.getY() - p1.getY())

    lstRectangleData[0] = fltLength * fltWidth
    lstRectangleData[1] = 2 * (fltWidth + fltLength)

    return lstRectangleData

def RenderInfo(GraphWinObj, lstRectangleData):

    Text(Point(200, 15), "Perimeter: {0:0.0f}".format(lstRectangleData[1])).draw(GraphWinObj)
    Text(Point(200, 35), "Area: {0:0.0f}".format(lstRectangleData[0])).draw(GraphWinObj)
    
def RenderButtons(GraphWinObj, lstButtonsData):

    for lstButton in lstButtonsData:

        ButtonShape = Rectangle(lstButton[1], lstButton[2])
        ButtonShape.setFill("khaki")
        ButtonShape.draw(GraphWinObj)

        fltUpperLeftX = lstButton[1].getX()
        fltUpperLeftY = lstButton[1].getY()
        fltLowerRightX = lstButton[2].getX()
        fltLowerRightY = lstButton[2].getY()

        fltCenterX = fltUpperLeftX + (fltLowerRightX - fltUpperLeftX) / 2
        fltCenterY = fltUpperLeftY + (fltLowerRightY - fltUpperLeftY) / 2
        Text(Point(fltCenterX, fltCenterY), lstButton[0]).draw(GraphWinObj)

def GetButtonClick(GraphWinObj, lstButtonsData):
    
    strClicked = ""
    
    while strClicked == "":
        
        fltMouse = GraphWinObj.getMouse()
        fltMouseX = fltMouse.getX()
        fltMouseY = fltMouse.getY()
        
        for lstButton in lstButtonsData:
            if ( (fltMouseX >= lstButton[1].getX()) and (fltMouseX <= lstButton[2].getX())
                 and (fltMouseY >= lstButton[1].getY()) and (fltMouseY <= lstButton[2].getY()) ):
                strClicked = lstButton[0]
                
    return strClicked

def main():

    lstConstButtonsData = [
        ["Reset", Point(110, 350), Point(190, 390)],
        ["Exit", Point(210, 350), Point(290, 390)],
    ]

    blnExit = False

    while blnExit == False:
        win = GraphWin("Rectangle Information", 400, 400)

        RenderInfo(win, GetRectangle(win))
        RenderButtons(win, lstConstButtonsData)
        ButtonClick = GetButtonClick(win, lstConstButtonsData)
        if ButtonClick == "Exit":
            blnExit = True

        win.close()

main()
