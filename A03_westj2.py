######################################################################
# Author: Johnathan West
# Username: westj2
#
# Assignment: A03
# Doc:https://docs.google.com/document/d/1iQCxEhiEbdHSGWJ16A9AC4E5ViTDvvYHfBGZpW7KiEQ/edit?usp=sharing
######################################################################
import turtle


def head():
    """draws the circle for the head"""
    jay = turtle.Turtle()
    jay.shape("turtle")
    jay.speed(0)
    jay.pensize(15)
    jay.pu()
    jay.right(90)
    jay.forward(270)
    jay.left(90)
    jay.pd()
    jay.fillcolor((232, 202, 179))
    jay.begin_fill()
    jay.circle(270, 360, None)
    jay.end_fill()
    jay.hideturtle()


def eyes():
    """draws the eyes of the face"""
    jay = turtle.Turtle()
    jay.speed(0)
    jay.pensize(15)
    jay.pu()
    jay.setpos(-90, 90)
    jay.left(160)
    jay.pd()
    jay.fillcolor(255, 0, 0)
    jay.begin_fill()
    jay.circle(150, 45, None)
    jay.left(132)
    jay.circle(150, 45, None)
    jay.end_fill()
    jay.hideturtle()
    shay = turtle.Turtle()
    shay.shape("turtle")
    shay.speed(0)
    shay.pensize(15)
    shay.pu()
    shay.setpos(180, 90)
    shay.left(160)
    shay.pd()
    shay.fillcolor(255, 0, 0)
    shay.begin_fill()
    shay.circle(150, 45, None)
    shay.left(132)
    shay.circle(150, 45, None)
    shay.end_fill()
    shay.hideturtle()


def nose():
    """draws the nose on the face"""
    boy = turtle.Turtle()
    boy.speed(0)
    boy.shape("turtle")
    boy.pensize(15)
    boy.pu()
    boy.setpos(-20, -20)
    boy.pd()
    boy.circle(50, 180)
    boy.hideturtle()


def mouth():
    """draws the mouth of the face"""
    bro = turtle.Turtle()
    bro.speed(0)
    bro.shape("circle")
    bro.pensize(15)
    bro.pu()
    bro.setpos(150, -140)
    bro.right(45)
    bro.pd()
    bro.circle(-200, -90, None)
    bro.hideturtle()


def mono():
    """draws the angry eyebrow of the face"""
    fore = turtle.Turtle()
    fore.speed(0)
    fore.shape("circle")
    fore.pensize(15)
    fore.pu()
    fore.setpos(-173, 185)
    fore.right(45)
    fore.pd()
    fore.circle(245, 90, None)
    fore.hideturtle()


def main():
    """draws the face of an angry man"""
    wn = turtle.Screen()
    wn.colormode(255)
    head()
    eyes()
    nose()
    mouth()
    mono()
    wn.exitonclick()


main()
