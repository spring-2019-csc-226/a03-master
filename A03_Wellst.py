#######################################################################################################################
# Taran Wells
# Wellst
# https://docs.google.com/document/d/1RBeOXjYBBjZ507wVeQVIPBrU7gBvTNJi8BYGDvtC53w/edit?usp=sharing
#######################################################################################################################

import turtle               # allows us to use the turtles library


wn = turtle.Screen()
wn.colormode(255)

# setup turtles
base = turtle.Turtle()
base.hideturtle()
roof = turtle.Turtle()
roof.hideturtle()
glass = turtle.Turtle
wn.bgcolor("red")


def house_base(t, sz):
    """Base of house"""

    t.color(250, 165, 10)     # house orange
    t.pendown()
    t.begin_fill()
    for side in range(2):
        t.forward(sz)
        t.right(90)             # square house
        t.forward(sz)
        t.right(90)
    t.end_fill()
    t.penup()


def house_roof(t1, sz):
    """Roof of house"""
    t1.color(135, 30, 160)       # roof purple
    t1.begin_fill()
    for side in range(3):
        t1.forward(sz)           # shape roof
        t1.left(120)
    t1.end_fill()
    t1.penup()


def placement(t2, sz):
    """place glass in starting position"""
    t2.fd(sz)
    t2.right(90)
    t2.fd(sz)


def house_window(t3):
    """window on house"""
    t3.begin_fill()
    t3.pendown()
    t3.pencolor('black')
    for side in range(4):
        t3.fd(35)
        t3.right(90)
    t3.fillcolor(30, 135, 160)      # make window light blue
    t3.end_fill()


def main():
    roof.penup()
    roof.back(30)
    roof.pendown()
    house_base(base, 140)
    placement(base, 70)
    house_roof(roof, 200)
    house_window(base)
    base.left(90)
    house_window(base)
    base.left(90)
    house_window(base)
    base.left(90)
    house_window(base)
    base.pu()
    base.left(90)
    base.fd(70)
    base.right(90)
    base.pd()
    base.begin_fill()
    for grass in range(2):
        base.fd(1000)
        base.left(90)
    base.fd(2000)
    base.left(90)
    base.fd(1000)
    base.left(90)
    base.fd(1000)
    base.fillcolor(0, 255, 0)
    base.end_fill()

main()     # calls on main function
wn.exitonclick()
