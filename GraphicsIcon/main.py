from graphics import *

class SketchBoard():

    def __init__(self, winObj):
        self.background = "white"
        self.shapes = []
        self.win = winObj

    def addShape(self, shapeObj):
        self.shapes.append(shapeObj)
        shapeObj.draw(self.win)

def main():

    winCanvas = GraphWin("Graphics Icon", 1200, 500)
    winCanvas.setBackground("white")

    winTool = GraphWin("Tool", 500, 500)


    sk = SketchBoard(winCanvas)

    run = True
    while run:
        pMouse = winCanvas.checkMouse()
        if pMouse != None:
            sk.addShape(pMouse)

    winCanvas.close()

main()