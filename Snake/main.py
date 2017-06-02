from random import randint
from time import sleep
from graphics import *

BODY_SIZE = 8
FOOD_SIZE = 8
GAME_CYCLE = 0.08

def reverse(h):
    if h == "up":
        return "down"
    elif h == "down":
        return "up"
    elif h == "left":
        return "right"
    elif h == "right":
        return "left"
    else:
        return ""

def overlap(p1, p2):
    if (p1.getX() == p2.getX()) and (p1.getY() == p2.getY()):
        return True
    return False

class Section:

    def __init__(self, p, GraphWinObj, h="up"):
        self.win = GraphWinObj
        self.Sprite = Circle(p, BODY_SIZE)
        self.Sprite.setFill("green")
        self.Sprite.setOutline("green")
        self.Sprite.draw(self.win)
        self.heading = h
        self.nextheading = h

class Snake:

    def __init__(self, p, GraphWinObj):
        self.win = GraphWinObj
        headpos = p
        self.body = [Section(headpos, self.win)]
        self.body[0].Sprite.setFill("blue")
        self.body[0].Sprite.setOutline("blue")
        headpos.move(0, BODY_SIZE * 2)
        self.body.append(Section(headpos, self.win))
        headpos.move(0, BODY_SIZE * 2)
        self.body.append(Section(headpos, self.win))

    def move(self):
        for i in range(len(self.body)):
            if self.body[i].heading == "up":
                self.body[i].Sprite.move(0, -BODY_SIZE * 2)
            if self.body[i].heading == "down":
                self.body[i].Sprite.move(0, BODY_SIZE * 2)
            if self.body[i].heading == "left":
                self.body[i].Sprite.move(-BODY_SIZE * 2, 0)
            if self.body[i].heading == "right":
                self.body[i].Sprite.move(BODY_SIZE * 2, 0)
            if i < len(self.body) - 1:
                self.body[i + 1].nextheading = self.body[i].heading
            self.body[i].heading = self.body[i].nextheading

    def turn(self, h):
        if (reverse(h) != "") and (reverse(h) != self.body[0].heading):
            self.body[0].heading = h
            self.body[0].nextheading = h
            self.body[1].nextheading = h
            return True
        else:
            return False

    def grow(self):
        lastSect = self.body[len(self.body) - 1]
        pCenter = lastSect.Sprite.getCenter()
        if lastSect.heading == "up":
            pCenter.move(0, BODY_SIZE * 2)
        if lastSect.heading == "down":
            pCenter.move(0, -BODY_SIZE * 2)
        if lastSect.heading == "left":
            pCenter.move(BODY_SIZE * 2, 0)
        if lastSect.heading == "right":
            pCenter.move(-BODY_SIZE * 2, 0)
        self.body.append(Section(pCenter, self.win, h=lastSect.heading))

    def collided(self):
        firstSectPos = self.body[0].Sprite.getCenter()
        result = False
        if ((firstSectPos.getX() < 0) or (firstSectPos.getX() > self.win.getWidth())
            or (firstSectPos.getY() < 0) or (firstSectPos.getY() > self.win.getHeight())):
            result = True
        for i in range(1, len(self.body)):
            sectPos = self.body[i].Sprite.getCenter()
            if overlap(sectPos, firstSectPos):
                result = True
                break
        return result

    def ate(self, food):
        firstSect = self.body[0].Sprite
        if overlap(food.Sprite.getCenter(), firstSect.getCenter()):
            return True
        else:
            return False

class Food:

    def __init__(self, GraphWinObj):
        self.win = GraphWinObj
        self.Sprite = Circle(Point(BODY_SIZE, BODY_SIZE), FOOD_SIZE)
        self.Sprite.setFill("red")
        self.Sprite.setOutline("red")
        self.Sprite.draw(self.win)
        self.Sprite.move(
            randint(0, self.win.getWidth() // BODY_SIZE // 2 - 1) * BODY_SIZE * 2,
            randint(0, self.win.getHeight() // BODY_SIZE // 2 - 1) * BODY_SIZE * 2
        )

def GameOver(GraphWinObj, score):
    msg = Text(Point(GraphWinObj.getWidth() / 2, 50), "Game Over\nScore: {}".format(score))
    msg.setTextColor("black")
    msg.setSize(15)
    msg.setStyle("bold")
    msg.draw(GraphWinObj)
    GraphWinObj.getMouse()

def main():

    win = GraphWin("Snake", 400, 400, autoflush=False)
    win.setBackground("khaki")
    snake = Snake(Point(win.getWidth() / 2, win.getHeight() / 2), win)
    food = Food(win)
    score = 0

    run = True
    while run:
        sleep(GAME_CYCLE)
        ctr = win.checkKey().lower()
        if (ctr == "p") or (ctr == "P"):
            win.getKey()
        if ctr != "":
            snake.turn(ctr)
        snake.move()
        if snake.ate(food):
            food.Sprite.undraw()
            food = Food(win)
            snake.grow()
            score += 1
        if snake.collided():
            run = False
        win.update()

    GameOver(win, score)

    win.close()

main()
