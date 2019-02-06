#################################################################################
# Author: Luis Riera
# Username: rieral
#
# Google Doc: https://docs.google.com/document/d/17osx_b7mNSBYE87tz3oM2N4at9yBHwu3gdz3AyqjKcw/edit?usp=sharing
# Assignment: A03
# Purpose:
#################################################################################

import turtle


def create_turtle(c, s):
    """
    Creates a turtle
    :param c: turtle's color
    :param s: turtle's size
    :return: returns the turtle object fully created
    """
    t = turtle.Turtle()
    t.pencolor(c)
    t.pensize(s)
    return t


def draw_square(t, l):
    """
    Draws a square of length l with turtle t
    :param t: turtle object
    :param l: int for the square sides
    :return:
    """
    for i in range(4):
        t.fd(l)
        t.right(90)


def draw_triangle(t, l):
    """
    Draws a triangle of size l with turtle t
    :param t: turtle object
    :param l: int for the triangle sides
    :return:
    """
    for i in range(3):
        t.fd(l)
        t.left(120)


def move_turtle(t, x, y):
    """
    Moves turtle t to coordinates (x,y)
    :param x: int for x coordinate
    :param y: int for y coordinate
    :param t: turtle object
    :return:
    """
    t.penup()
    t.setpos(x, y)
    t.pendown()


def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.colormode(255)

    luis = create_turtle((150, 75, 80), 5)
    # draw a big square for the house
    draw_square(luis, 200)
    # draw the roof
    draw_triangle(luis, 200)
    # moves turtle and draws windows
    move_turtle(luis, 20, -60)
    draw_square(luis, 50)
    move_turtle(luis, 130, -60)
    draw_square(luis, 50)
    # moves turtle and draws a door
    move_turtle(luis, 75, -150)
    draw_square(luis, 50)

    wn.exitonclick()


main()
