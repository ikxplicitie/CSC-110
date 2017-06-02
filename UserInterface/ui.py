from graphics import *

class Button:

    def __init__(self, label_string, p1, p2):

        self.TYPE = "Button"
        self.name = label_string
        self.visible = False

        self.label = label_string
        self.shape = Rectangle(p1, p2)
        self.text = Text(self.shape.getCenter(), self.label)

    def draw(self, win_obj):
        self.shape.draw(win_obj)
        self.text.draw(win_obj)
        self.visible = True

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
        self.visible = False

    def update(self, win_obj):
        self.undraw()
        self.draw(win_obj)

    def checkMouse(self, p_mouse):

        mouseX = p_mouse.getX()
        mouseY = p_mouse.getY()
        buttomUpperLeftX = self.shape.p1.getX()
        buttonUpperLeftY = self.shape.p1.getY()
        buttomLowerRightX = self.shape.p2.getX()
        buttonLowerRightY = self.shape.p2.getY()

        if ((mouseX > buttomUpperLeftX) and (mouseX < buttomLowerRightX)) and ((mouseY > buttonUpperLeftY) and (mouseY < buttonLowerRightY)):
            return True
        else:
            return False


class UserInterface:

    def __init__(self):

        self.TYPE = "User Interface"
        self.name = ""

        self.visible = False
        self.elements = []

    def add(self, ui_obj):
        self.elements.append(ui_obj)

    def rem(self, obj_name):
        for i in range(len(self.elements)):
            if self.elements[i].name == obj_name:
                self.elements.pop(i)

    def draw(self, win_obj):
        for obj in self.elements:
            obj.draw(win_obj)
        self.visible = True

    def undraw(self):
        for obj in self.elements:
            obj.undraw()
        self.visible = False

    def update(self, win_obj):
        self.undraw()
        self.draw(win_obj)

    def checkMouse(self, p_mouse):
        for obj in self.elements:
            if obj.checkMouse(p_mouse) == True:
                return obj.name
        return ""
