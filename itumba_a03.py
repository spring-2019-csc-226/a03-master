######################################################################
# Author: Nicole Itumba
# Username: Itumban_A03
#GoogleDoc: https://docs.google.com/document/d/15V7Bk_zvKYsn6cmAq_iV8ZQVYu4eXKbd3beAlwDjre4/edit?usp=sharing
#
# Assignment: T03: Boustrophedon Turtles and Functions
# Purpose: To very simply demonstrate the turtle library to demo shapes and using images for shapes
######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
#
# Dr. Jan Pearce - this file is modified from her original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle               # allows us to use the turtles library

def draw_rectangle(tablet):
    """
    This is the part that draws the rectangle of the tablet
    """
    tablet.begin_fill()
    for i in range(4):

        tablet.forward(250)
        tablet.left(90)
    tablet.end_fill()
    """"
    Creates the inner screen of the tablet
    """
    tablet.penup()
    tablet.goto(125, 0)
    tablet.pendown()
    tablet.color("blue")
    tablet.circle(10,360,40)

    tablet.penup()
    tablet.goto(30,40)
    tablet.pendown()

    tablet.begin_fill()
    for i in range(4):
        tablet.forward(190)
        tablet.left(90)
    tablet.end_fill()
    tablet.begin_fill()

    tablet.penup()
    tablet.goto(110,200)
    tablet.color("red")
    tablet.pendown()

    """ create the camera button of the tablet
    """
    for i in range(4):
        tablet.forward(30)
        tablet.left(90)
    tablet.end_fill()



def main():
    """
    This is the main function
    :return:
    """
    wn = turtle.Screen()
    wn.bgcolor("red")

    tablet = turtle.Turtle()
    tablet.color("#A1A1A1")
    draw_rectangle(tablet)

    wn.exitonclick()

main()



