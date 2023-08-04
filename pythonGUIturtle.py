
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

for i in range(3):
    taoCicle()
    tao.penup()
    tao.goto(random.randint(-960,960),random.randint(-540,540))
    tao.pendown()
    rectangle()
    tao.penup()
    tao.goto(random.randint(-960,960),random.randint(-540,540))
    tao.pendown()

