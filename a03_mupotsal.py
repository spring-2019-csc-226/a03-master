#################################################################################
# Author: Liberty Mupotsa
# Username: mupotsal
# Google document link to the file :
# https://docs.google.com/document/d/1LkTHFrehbfiPwt7vFb3iw_GgT8vMh2vvjSVyskBteDg/edit?usp=sharing
# Assignment:A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learning more about turtle functions and methods.
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle


wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor((238, 130, 238))
lb = turtle.Turtle()
lb.color("green")
lb.pensize(10)
zz = turtle.Turtle()
zz.color("yellow")


def make_the_front ():
    """this function makes the front part of the house which is basically a square"""
    lb.pu()
    lb.goto(-100, -100)
    lb.pd()
    for i in range(2):
        lb.filling()
        lb.fillcolor("white")
        lb.begin_fill()
        lb.forward(400)
        lb.left(90)
        lb.forward(200)
        lb.left(90)
        lb.end_fill()


def make_the_right_side():
    lb.pu()
    lb.goto(290, -100)
    lb.left(43)
    lb.pd()
    lb.fd(150)
    lb.right(-45)
    lb.fd(100)
    lb.left(-90)
    lb.forward(1)
    lb.left(-180)
    lb.fd(100)



def make_roof():
    lb.filling()
    lb.begin_fill()
    lb.fillcolor("red")
    lb.penup()
    lb.goto(-100,100)
    lb.pd()
    lb.right(-230)
    lb.forward(150)

    lb.rt(45)
    lb.fd(410)
    lb.rt(135)
    lb.forward(180)
    lb.end_fill()
    lb.filling()
    lb.begin_fill()
    lb.fillcolor('white')
    lb.forward(-180)
    lb.left(100)
    lb.forward(160)
    lb.right(60)
    lb.forward(150)
    lb.rt(65)
    lb.fd(255)
    lb.end_fill()
def door ():
    lb.penup()
    lb.goto(60,-100)
    lb.pd()
    lb.rt(110)
    for i in range (1):
        lb.filling()
        lb.begin_fill()
        lb.fillcolor("purple")
        lb.forward(100)
        lb.rt(90)
        lb.forward(50)
        lb.right(90)
        lb.fd(99)
        lb.end_fill()

def window ():
    lb.filling()
    lb.fillcolor('red')
    lb.begin_fill()
    lb.pu()
    lb.goto(150,20)
    lb.pd()
    for i in range (4):
        lb.forward(70)
        lb.left(90)
    lb.end_fill()
    lb.pu()


def make_window():
    lb.filling()
    lb.fillcolor('red')
    lb.begin_fill()

    lb.goto(-50, 20)
    lb.pd()
    for i in range(4):
        lb.forward(70)
        lb.left(90)
    lb.end_fill()







def make_star ():

    zz.pu()
    zz.goto(-200,-300)
    zz.pd()
    zz.filling()
    zz.fillcolor('red')
    zz.begin_fill()
    for i in range (4):
        for i in range(10):
            zz.forward(200)
            zz.left(45)
            zz.left(120)
    zz.end_fill()
    zz.write("Forward we go Forever!!!!!!")





















def main():
    make_the_front()
    make_the_right_side()
    make_roof()
    door()
    window()
    make_window()
    make_star()


    wn.exitonclick()



main()


