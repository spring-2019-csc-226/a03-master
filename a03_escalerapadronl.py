#################################################################################
# Author: Lisandro Padron
# Username: escalerapadronl
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic  Robotic Turtles
# Link: https://docs.google.com/document/d/1gMddsifPMImntv5zzTSnBIvh6N03kJfG7NIatMYG7ok/edit#
# Purpose: Learning how to define and call functions.
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
wn = turtle.Screen()
wn.colormode(255)  # allows the program to use RGB
wn.bgcolor(246, 79, 47)


# declarations
martin = turtle.Turtle()
martin.speed(0)
martin.setheading(0)
martin.color(215, 215, 215)

roberto = turtle.Turtle()
roberto.speed(0)
roberto.color('black')
roberto.pensize(5)
roberto.setheading(0)

gerardo = turtle.Turtle()
gerardo.speed(0)
gerardo.setheading(90)
gerardo.color(118, 57, 49)
gerardo.pensize(5)

jose = turtle.Turtle()
jose.speed(0)
jose.setheading(90)
jose.color(185, 156, 107)

lisandro = turtle.Turtle()
lisandro.speed(0)
lisandro.setheading(180)
lisandro.color(243, 188, 46)


def draw_pavement():
    """
    This draws out the pavement.
    :return:
    """

    roberto.penup()
    roberto.goto(-345, -100)
    roberto.pendown()
    roberto.begin_fill()
    for i in range(4):  # this loop draws a big black rectangle that is positioned at the bottom part of the screen
        roberto.forward(684)
        roberto.right(90)
    roberto.end_fill()


def draw_building():
    """
    This draws out the building.
    :return:
    """

    gerardo.penup()
    gerardo.backward(135)
    gerardo.pendown()
    gerardo.begin_fill()
    for i in range(2):  # this loop draws out the rectangle for the building
        gerardo.forward(200)
        gerardo.right(90)
        gerardo.forward(100)
        gerardo.right(90)
    gerardo.end_fill()
    gerardo.hideturtle()


def draw_windows():
    """
    This draws out a window.
    :return:
    """
    martin.begin_fill()  # lines 88-118 draw out a row consisting of 3 rectangles for windows
    for i in range(2):
        martin.pendown()
        martin.forward(13)
        martin.right(90)
        martin.forward(20)
        martin.right(90)
        martin.penup()
    martin.end_fill()

    martin.forward(30)
    martin.begin_fill()
    for i in range(2):
        martin.pendown()
        martin.forward(13)
        martin.right(90)
        martin.forward(20)
        martin.right(90)
        martin.penup()
    martin.end_fill()

    martin.forward(30)
    martin.begin_fill()
    for i in range(2):
        martin.pendown()
        martin.forward(13)
        martin.right(90)
        martin.forward(20)
        martin.right(90)
        martin.penup()
    martin.end_fill()
    martin.hideturtle()


def draw_door():
    """
    This draws out a door.
    :return:
    """

    jose.penup()
    jose.goto(38, -137)
    jose.pendown()
    jose.begin_fill()
    for i in range(2):  # this loop draws a rectangle for the door of the building.
        jose.forward(40)
        jose.right(90)
        jose.forward(20)
        jose.right(90)
    jose.end_fill()
    jose.hideturtle()


def draw_sun():
    """
    This draws out the sun.
    :return:
    """
    lisandro.penup()
    lisandro.goto(40, 90)
    lisandro.begin_fill()
    lisandro.circle(150)  # draws out a circle with a radius of 150 for the sun.
    lisandro.end_fill()
    lisandro.hideturtle()


def draw_doorknob():
    lisandro.color('black')
    lisandro.goto(55, -115)
    lisandro.begin_fill()
    lisandro.circle(2)  # draws out a black circle with a radius of 2 for the doorknob.
    lisandro.end_fill()
    lisandro.hideturtle()


def main():
    """
    This function runs calls all of the functions all at once.
    :return:
    """
    draw_sun()
    draw_pavement()
    draw_building()
    martin.goto(12, 40)  # lines 171, 173, and 175 move the turtle down to space out the windows on the building.
    draw_windows()
    martin.goto(12, 0)
    draw_windows()
    martin.goto(12, -40)
    draw_windows()
    draw_door()
    draw_doorknob()


main()
wn.exitonclick()