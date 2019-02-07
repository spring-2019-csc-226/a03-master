##########################################################################################################################
# Author: Megan Grey
# Username: greym
#
# Assignment: A03
# https://docs.google.com/document/d/1LNhwkD7_GoYJS8iZDrmhv2H5phi5jR41Nj9yr7PZjfk/edit?usp=sharing
##########################################################################################################################

import turtle
wn = turtle.Screen()
turtle.bgcolor("#00bfff")


def draw_wing1(turt):
    """Draws wing on plane"""
    turt.fillcolor("gray")
    turt.penup()
    turt.forward(150)
    turt.left(90)
    turt.forward(70)
    turt.right(150)
    turt.pendown()
    turt.begin_fill()
    turt.forward(180)
    turt.circle(25,150)
    turt.forward(160)
    turt.end_fill()

def draw_wing2(turt):
    """Draws second wing on other side of plane"""
    turt.fillcolor("dark gray")
    turt.penup()
    turt.left(65)
    turt.forward(260)
    turt.left(90)
    turt.forward(135)
    turt.left(40)
    turt.pendown()
    turt.begin_fill()
    turt.fd(50)
    turt.circle(25,150)
    turt.fd(50)
    turt.end_fill()

def draw_body(turt):
    """Draws body of a plane"""
    turt.fillcolor("gray")
    turt.begin_fill()
    turt.left(18)
    turt.forward(400)
    turt.circle(70,180)
    turt.left(12)
    turt.forward(400)
    turt.circle(29,160)
    turt.end_fill()

def draw_tail(turt):
    """Draw tail of plane"""
    turt.fillcolor("gray")
    turt.penup()
    turt.left(90)
    turt.forward(225)
    turt.right(40)
    turt.pendown()
    turt.begin_fill()
    turt.forward(90)
    turt.circle(30,150)
    turt.forward(75)
    turt.end_fill()

def draw_window(turt):
    """Draws cockpit window on plane"""
    turt.fillcolor("white")
    turt.penup()
    turt.left(100)
    turt.fd(235)
    turt.left(180)
    turt.pendown()
    turt.begin_fill()
    turt.fd(50)
    turt.left(90)
    turt.fd(40)
    turt.left(90)
    turt.fd(77)
    turt.end_fill()

def draw_nose(turt):
    """Draws nose on plane"""
    turt.fillcolor("gray")
    turt.begin_fill()
    turt.fd(40)
    for i in range(8):
        turt.right(15)
        turt.fd(10)
    turt.right(25)
    turt.fd(25)
    turt.right(30)
    turt.fd(90)
    turt.end_fill()

def draw_windows(turt):
    """draws four circular windows on body of plane """
    turt.fillcolor("white")
    turt.penup()
    turt.right(55)
    turt.fd(120)
    turt.pendown()
    turt.begin_fill()
    turt.circle(14)
    turt.end_fill()

    turt.penup()
    turt.left(45)
    turt.fd(60)
    turt.pendown()
    turt.begin_fill()
    turt.circle(14)
    turt.end_fill()

    turt.penup()
    turt.left(5)
    turt.fd(60)
    turt.pendown()
    turt.begin_fill()
    turt.circle(14)
    turt.end_fill()

    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.begin_fill()
    turt.circle(14)
    turt.end_fill()

def draw_cloud(turt):
    """draws a cloud"""
    turt.penup()
    turt.left(65)
    turt.fd(250)
    turt.left(90)
    turt.forward(200)
    turt.pendown()

    turt.color("white")
    turt.begin_fill()
    turt.fd(150)
    for i in range(5):
        turt.circle(30,180)
        turt.right(135)
    turt.end_fill()

    turt.penup()
    turt.right(90)
    turt.forward(520)
    turt.right(135)
    turt.pendown()

    turt.begin_fill()
    turt.fd(150)
    for i in range(5):
        turt.circle(30, 180)
        turt.right(135)
    turt.end_fill()


def main():
    """Main function"""
    John = turtle.Turtle()
    John.pensize(5)
    John.speed(0)
    John.penup()
    John.right(90)
    John.forward(50)
    John.left(90)
    John.backward(250)
    John.pendown()
    draw_body(John)
    draw_wing1(John)
    draw_tail(John)
    draw_wing2(John)
    draw_window(John)
    draw_nose(John)
    draw_windows(John)
    draw_cloud(John)

main()
wn.exitonclick()
