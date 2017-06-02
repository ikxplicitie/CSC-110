from graphics import *


def main():
    win = GraphWin("ABC", 400, 300)

    # Draw the add button
    Addbutton = Rectangle(Point(35, 60), Point(80, 80))
    Addbutton.setFill("white")
    Addbutton.draw(win)

    # Draw the text
    WordsOfAdd = Text(Point(55, 70), "Add")
    WordsOfAdd.draw(win)
    WordsOfAdd.setFace("arial")
    WordsOfAdd.setSize(14)
    WordsOfAdd.setTextColor("black")

    # Prompt the user to input the first number
    entInputNo1 = Entry(Point(60, 135), 5)
    entInputNo1.setText("0")
    entInputNo1.draw(win)

    # Creat the plus sign
    Plus1 = Rectangle(Point(100, 125), Point(105, 140))
    Plus1.setFill("black")
    Plus1.draw(win)

    Plus2 = Rectangle(Point(95, 130), Point(111, 135))
    Plus2.setFill("black")
    Plus2.draw(win)

    # Creat the equal sign
    Equal1 = Rectangle(Point(190, 128), Point(210, 132))
    Equal1.setFill("black")
    Equal1.draw(win)

    Equal2 = Rectangle(Point(190, 138), Point(210, 142))
    Equal2.setFill("black")
    Equal2.draw(win)

    # Prompt the user to input the second number
    entInputNo2 = Entry(Point(150, 135), 5)
    entInputNo2.setText("0")
    entInputNo2.draw(win)

    # Calculate and print the sum of 2 numbers
    win.getMouse()
    fltFirstNumber = float(entInputNo1.getText())
    fltSecondNumber = float(entInputNo2.getText())
    fltSum = fltFirstNumber + fltSecondNumber
    Output = Text(Point(240, 135), "")
    Output.setText(fltSum)
    Output.setTextColor("Salmon")
    Output.setSize(20)
    Output.draw(win)


main()