
import turtle
import random
tao = turtle.Pen()
tao.shape("turtle")
taoColor = ["red","green","yellow","blue","black","grey"]


def rectangle():
    for i in range(24):
        tao.forward(50)
        tao.color(random.choice(taoColor))
        tao.left(90)
        tao.forward(50)
        tao.color(random.choice(taoColor))
        tao.left(90)
        tao.forward(50)
        tao.color(random.choice(taoColor))
        tao.left(90)
        tao.forward(50)
        tao.color(random.choice(taoColor))
        tao.left(15)
    

def taoCicle():
    for i in range(24):
        tao.circle(75)
        tao.left(15)
        tao.color(random.choice(taoColor))

def taoTriangle():
    for i in range(24):
        tao.forward(75)
        tao.left(135)
        tao.color(random.choice(taoColor))
        tao.forward(75)
        tao.left(135)
        tao.color(random.choice(taoColor))
        tao.forward(75)
        tao.left(15)

for i in range(3):
    taoCicle()
    tao.penup()
    tao.goto(random.randint(-800,800),random.randint(-500,500))
    tao.pendown()
    rectangle()
    tao.penup()
    tao.goto(random.randint(-800,800),random.randint(-500,500))
    tao.pendown()
    taoTriangle()
    tao.penup()
    tao.goto(random.randint(-800,800),random.randint(-500,500))
    tao.pendown()

