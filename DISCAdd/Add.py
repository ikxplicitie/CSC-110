# Add - Mike Vo
# Description: This program prompt user for 2 number from 2 text
#              entries and add them up and display the result
#              after user press a button

from graphics import *

# Check if a button has been pressed by user (return a boolean)
def buttonPressed(buttonShapeObj, GraphWinObj):

    mouse = GraphWinObj.getMouse()

    p1 = buttonShapeObj.getP1()
    p2 = buttonShapeObj.getP2()

    if ( ((mouse.getX() > p1.getX()) and (mouse.getX() < p2.getX()))
        and ((mouse.getY() > p1.getY()) and (mouse.getY() < p2.getY())) ):
        return True

    return False

def main():

    # Inititalize a white background window
    win = GraphWin("Add", 300, 200)
    win.setBackground("white")

    # Display instruction
    message = Text(Point(150, 35), "Enter two values, then press \"Add\"\nto see the result")
    message.draw(win)

    # Initialize and display the 2 entries
    numberEntry1 = Entry(Point(50, 100), 5)
    numberEntry1.setTextColor("white")
    numberEntry1.draw(win)
    numberEntry2 = Entry(Point(130, 100), 5)
    numberEntry2.setTextColor("white")
    numberEntry2.draw(win)

    # Decorations
    Text(Point(90, 100), "+").draw(win)
    Text(Point(175, 100), "=").draw(win)

    # Initialize and display the "Add" button
    buttonShape = Rectangle(Point(120, 150), Point(180, 175))
    buttonShape.setFill("khaki")
    buttonShape.draw(win)
    buttonLabel = Text(buttonShape.getCenter(), "Add")
    buttonLabel.draw(win)

    # Pause the program for user input
    blnWait = True
    while blnWait:
        # When user press "Add" button
        if buttonPressed(buttonShape, win):
            # Check if any entry is empty
            if (numberEntry1.getText() != "") and (numberEntry2.getText() != ""):
                # Un-Pause
                blnWait = False
            else:
                # Update message with a warning
                message.setText("Entry must not be empty!\nEnter two values, then press \"Add\"\nto see the result")

    # Display result and update instruction
    Text(Point(225, 100), "{0:0.2f}".format(float(numberEntry1.getText()) + float(numberEntry2.getText()))).draw(win)
    message.setText("Click anywhere to quit")

    # Wait for user to click anywhere
    win.getMouse()

    # Close window
    win.close()

main()