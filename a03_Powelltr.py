######################################################################
# Author: Trent Powell
# Username: Powelltr
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To further our understanding of turtles, loops, and more complex programming projects
#
# Google Doc: https://docs.google.com/document/d/19k3zkhOs8GC1BVng44AMsnLKEfaAOMUn1zgBTiLYYs0/edit?usp=sharing
######################################################################

import turtle


def draw_tv(b):
    """
    This will draw the tv in the center of the screen

    """
    b.setpos(250, 125)
    b.pensize(10)
    b.left(180)
    b.pendown()
    b.begin_fill()
    for i in range(2):          # draws the basic outline of tv
        b.forward(500)
        b.left(90)
        b.forward(250)
        b.left(90)
    b.end_fill()
    b.penup()
    b.setpos(-20, -125)
    b.pendown()
    b.left(90)
    b.color("black")
    b.begin_fill()
    for i in range(2):          # draws the IR receiver
        b.forward(20)
        b.left(90)
        b.forward(40)
        b.left(90)
    b.end_fill()
    b.penup()
    b.setpos(-145, -125)
    b.pendown()
    b.right(45)
    b.forward(45)
    b.left(45)
    b.penup()
    b.setpos(145, -125)         # draws the tv stand legs
    b.pendown()
    b.left(45)
    b.forward(45)
    b.right(45)
    b.penup()
    b.pencolor("red")           # creates the power on indicator on ir receiver
    b.setpos(0, -134)
    b.pensize(8)
    b.pendown()
    b.forward(1)


def draw_hulu(r):
    """
    This will draw the 'HULU' on the tv screen

    """
    r.setpos(-150, 50)          # draws the H
    r.seth(270)
    r.pensize(20)
    r.pendown()
    r.forward(100)
    r.seth(90)
    r.forward(50)
    r.seth(0)
    r.forward(40)
    r.seth(90)
    r.forward(50)
    r.seth(270)
    r.forward(100)              # end H
    r.penup()
    r.setpos(-65, 50)           # draws the first U
    r.seth(270)
    r.pendown()
    r.forward(100)
    r.seth(0)
    r.forward(40)
    r.seth(90)
    r.forward(100)              # end U1
    r.penup()
    r.setpos(25, 50)            # draws the L
    r.seth(270)
    r.pendown()
    r.forward(100)
    r.seth(0)
    r.forward(40)               # end L
    r.penup()
    r.setpos(115, 50)           # draws the second U
    r.seth(270)
    r.pendown()
    r.forward(100)
    r.seth(0)
    r.forward(40)
    r.seth(90)
    r.forward(100)               # end U2
    r.penup()


def draw_table(m):
    """
    draws the table for the tv to sit on

    """
    m.setpos(-300, -288)
    m.seth(90)
    m.right(25)
    m.pensize(15)
    m.pendown()
    m.forward(130)
    m.penup()
    m.setpos(300, -288)
    m.seth(90)
    m.left(25)
    m.pendown()
    m.forward(130)
    m.seth(0)
    m.forward(15)
    m.seth(180)
    m.forward(525)
    m.penup()


def main():
    draw_tv(barry)
    draw_hulu(rick)
    draw_table(morty)


barry = turtle.Turtle()             # creates the turtle 'barry' along with its settings
barry.color("light green")
barry.hideturtle()
barry.penup()
barry.pencolor("black")

rick = turtle.Turtle()              #
rick.pencolor("white")
rick.hideturtle()
rick.penup()

morty = turtle.Turtle()
morty.pencolor("brown")
morty.hideturtle()
morty.penup()


wn = turtle.Screen()
wn.bgcolor("navy")

main()

wn.exitonclick()
